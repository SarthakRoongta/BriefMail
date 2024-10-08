
function extractEmailContent() {
  let emailBody = document.querySelector('.ii.gt').innerText || "Email content not found.";
  return emailBody;
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "get_email_content") {
    let emailContent = extractEmailContent();
    sendResponse({ emailContent: emailContent });
  }
});
