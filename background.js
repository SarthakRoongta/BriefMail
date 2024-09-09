
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "summarize_email") {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.tabs.sendMessage(tabs[0].id, { action: "get_email_content" }, function(response) {
        if (response.emailContent) {
          sendResponse({ emailContent: response.emailContent });
        } else {
          sendResponse({ emailContent: null });
        }
      });
    });
    return true;
  }
});
