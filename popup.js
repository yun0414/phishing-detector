document.addEventListener("DOMContentLoaded", () => {

    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        if (tabs.length === 0) return;
    
        let currentTab = tabs[0];
    
        if (!currentTab.url.includes("mail.google.com")) {
            document.getElementById("status").innerText = "請開啟 Gmail";
            return;
        }
    
        chrome.tabs.sendMessage(currentTab.id, { type: "requestPhishingData" }, (response) => {
            if (chrome.runtime.lastError) {
                console.error("❌ 錯誤:", chrome.runtime.lastError);
                document.getElementById("status").innerText = "無法獲取數據";
                return;
            }
        
            if (!response || response.status !== "ok") {
                console.warn("⚠️ 未收到正確回應");
                document.getElementById("status").innerText = "未收到數據";
                return;
            }
        
            console.log(`✅ 成功獲取數據: 標題 ${response.subjectCount} / 寄件者 ${response.senderCount} / 內文 ${response.bodyCount}`);
        
            document.getElementById("status").innerHTML = `
                <p>標題異常: ${response.subjectCount} 封</p>
                <p>寄件者異常: ${response.senderCount} 封</p>
                <p>內文異常: ${response.bodyCount} 封</p>

            `;
        });
        
    });
});