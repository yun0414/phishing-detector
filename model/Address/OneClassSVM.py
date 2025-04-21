import pandas as pd
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
import re

df = pd.read_csv('phishing_urls.csv')

urls = df['url']

def extract_features(url):
    return {
        'url_length': len(url),
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'num_slashes': url.count('/'),
        'has_at': int('@' in url),
        'has_https': int('https' in url),
        'has_ip': int(bool(re.search(r'(\d{1,3}\.){3}\d{1,3}', url))),
    }

features = pd.DataFrame([extract_features(u) for u in urls])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)


model = OneClassSVM(kernel='rbf', nu=0.1, gamma='scale')
model.fit(X_scaled)
y_pred = model.predict(X_scaled)


normal_urls = [
    'https://www.google.com',
    'https://www.wikipedia.org',
    'https://www.openai.com',
    'http://allegrolokalnie.pl-84382019'
]

normal_features = pd.DataFrame([extract_features(u) for u in normal_urls])
normal_scaled = scaler.transform(normal_features)
y_test_pred = model.predict(normal_scaled)

print('預測結果（正常網址）：', y_test_pred)
