import pandas as pd
import numpy as np
import re
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from keras.models import Model
from keras.layers import Input, Dense

data = pd.read_csv("phishing_urls.csv")
urls = data['url']

blacklist_keywords = [".rest", ".cfd", "allegrolokalnie", "allegro.pl-"]

def is_blacklisted(url):
    return int(any(kw in url for kw in blacklist_keywords))

def extract_features(url):
    features = {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'num_digits': len(re.findall(r'\d', url)),
        'has_https': int('https' in url),
        'has_at': int('@' in url),
        'has_ip': int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url))),
        'has_suspicious_tld': int(any(url.endswith(ext) for ext in ['.rest', '.cfd', '.top', '.xyz'])),
        'starts_with_http': int(url.startswith('http')),
        'contains_blacklist_word': is_blacklisted(url),
    }
    return list(features.values())

features_list = [extract_features(url) for url in urls]
X = np.array(features_list)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

input_dim = X_scaled.shape[1]
encoding_dim = 5

input_layer = Input(shape=(input_dim,))
encoded = Dense(encoding_dim, activation='relu')(input_layer)
decoded = Dense(input_dim, activation='linear')(encoded)

autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mse')

autoencoder.fit(X_scaled, X_scaled, epochs=20, batch_size=128, shuffle=True)

def predict_url(url):
    if is_blacklisted(url):
        return "Phishing (blacklist)"
    feats = np.array([extract_features(url)])
    feats_scaled = scaler.transform(feats)
    recon = autoencoder.predict(feats_scaled)
    mse = np.mean(np.square(feats_scaled - recon))
    threshold = 0.5 
    return "Phishing (autoencoder)" if mse > threshold else "Legit"

test_urls = [
    "http://allegrolokalnie.pl-84382019.rest",
    "https://www.google.com",
    "http://example.pl-123456"
]

for u in test_urls:
    print(f"{u} => {predict_url(u)}")