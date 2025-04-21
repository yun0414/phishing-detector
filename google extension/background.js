chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === "complete" && tab.url) {
        console.log("🌐 新網頁載入，重置偵測結果...");
        chrome.storage.local.set({ suspiciousEmails: [] }); // 清空儲存的可疑郵件
    }
});
