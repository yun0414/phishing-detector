## 版本更新紀錄
前面時間都在研究多篇論文要如何利用AI model 去偵測釣魚信件
2025/03/25
train 一版本的模型但發現train壞掉了
目前還沒有想法哪裡有問題
[phishing-detector 1.0](https://github.com/MocuAcqu/Chrome_test/tree/main/phishing-detector)
功能：偵測信件標題是否有釣魚文案字樣，並可以成功計數信件異常標題
![image](https://hackmd.io/_uploads/SJcVAc-T1e.png)

2025/03/26
[phishing-detector 2.0](https://github.com/yun0414/phishing-detector/tree/main)
功能更新：
引入線上的釣魚網址資料集，轉換為csv檔案，透過flask去創建一個port專門讀取此csv檔案，再將檔案內的釣魚網址傳入進contents.js中的phishingURLs作為讀取的資料，如果釣魚網址出現在信件標題也會被標示出來
![image](https://hackmd.io/_uploads/HkHIXsWTke.png)
