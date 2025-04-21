## 版本更新紀錄
前面時間都在研究多篇論文要如何利用AI model 去偵測釣魚信件

2025/03/25

［進度更新］
train 一版本的模型但發現train壞掉了
目前還沒有想法哪裡有問題
[phishing-detector 1.0](https://github.com/MocuAcqu/Chrome_test/tree/main/phishing-detector)
功能：偵測信件標題是否有釣魚文案字樣，並可以成功計數信件異常標題

![image](https://hackmd.io/_uploads/SJcVAc-T1e.png)

2025/03/26

[phishing-detector 2.0](https://github.com/yun0414/phishing-detector/tree/main)
［進度更新］引入線上的釣魚網址資料集，轉換為csv檔案，透過flask去創建一個port專門讀取此csv檔案，再將檔案內的釣魚網址傳入進contents.js中的phishingURLs作為讀取的資料，如果釣魚網址出現在信件標題也會被標示出來

![image](https://hackmd.io/_uploads/HkHIXsWTke.png)

2025/04/10

［進度更新］model與資料集部分，尚未進入到插件串接的部分
篩選出一個全為釣魚網址的資料集phishing_urls.csv檔案
train了一版OneClassSVM去區分是否為釣魚網址
結果：比上一版利用隨機森林train的部分結果還要好，但還是較為無法偵測亂數產生的網址

2025/04/16

［進度更新］model部分
train了一版Autoencoder去區分是否為釣魚網址
結果：比OneClassSVM還要更好 讚的

2025/04/21

［進度更新］把目前現有的model與google extension的插件做結合，但尚未實作完成
