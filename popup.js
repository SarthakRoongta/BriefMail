
document.getElementById('summarizeBtn').addEventListener('click', () => {
  chrome.runtime.sendMessage({ action: "summarize_email" }, function(response) {
    if (response.emailContent) {
      // Send email content to Flask API for summarization
      fetch('http://localhost:5001/summarize', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: response.emailContent })
      })
      .then(res => res.json())
      .then(data => {
        // Display the summary returned by the NLP API
        document.getElementById('summary').innerText = data.summary;
      })
      .catch(error => {
        console.error('Error:', error);
        document.getElementById('summary').innerText = "Error processing summary.";
      });
    } else {
      document.getElementById('summary').innerText = "Email content could not be found.";
    }
  });
});
