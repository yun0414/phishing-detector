document.addEventListener("DOMContentLoaded", function () {
    
    // 先清除儲存的數據，確保每次打開 popup 時 UI 先重置
    //chrome.storage.local.clear();

    let scanButton = document.getElementById("scanEmails");

    scanButton.addEventListener("click", function () {
        //let emailList = document.getElementById("emailList");
        //let count = document.getElementById("count");
        
        // 清空 UI
        //emailList.innerHTML = "";
        //count.textContent = "*未知*";

        // 發送訊息給 content script 開始偵測郵件
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            chrome.tabs.sendMessage(tabs[0].id, { action: "scanEmails" });
        });
    });

    // 當 chrome.storage.local 變更時更新
    chrome.storage.onChanged.addListener((changes, areaName) => {
        if (areaName === "local" && changes.suspiciousEmails) {
            updatePopupData();
        }
    });
});

function updatePopupData() {
    chrome.storage.local.get("suspiciousEmails", function (data) {
        let emailList = document.getElementById("emailList");
        let count = document.getElementById("count");
        let emails = data.suspiciousEmails || [];

        if (emails.length === 0) {
            //emailList.innerHTML = "<li class='safe'>請開始偵測Gmail的信件</li>";
            return;
        }

        // 顯示異常信件數量（除以 2）
        count.textContent = Math.floor(emails.length / 2);
        
        // 統計標題出現次數
        let emailCounts = {};
        emails.forEach(title => {
            emailCounts[title] = (emailCounts[title] || 0) + 1;
        });

        // 顯示異常標題及次數（將次數除以 2）
        for (let title in emailCounts) {
            let li = document.createElement("li");
            // 顯示每個標題的數量減半
            li.textContent = `${title}  (${Math.floor(emailCounts[title]/2)} 封)`;
            emailList.appendChild(li);
        }
    });

}

