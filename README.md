
# Email Summarizer Chrome Extension

This Chrome extension uses Natural Language Processing (NLP) to summarize long email threads. It extracts the most important points, such as deadlines, tasks, and key takeaways, by sending email content to a Flask-based API for processing.

## Features
- Extracts key points from long email threads.
- Uses NLP (via spaCy) to analyze and summarize email content.
- Simple Chrome extension with a button to summarize emails.

## Files
- **manifest.json**: Chrome extension manifest.
- **popup.html**: HTML for the extension popup.
- **popup.js**: JavaScript that handles sending email content to the Flask API for summarization.
- **content.js**: Script to extract email content from Gmail.
- **background.js**: Manages the communication between the popup and content scripts.
- **email_summarizer_api.py**: Flask-based API that processes email content using spaCy and returns a summary.

## Setup
### Prerequisites
- Python 3.x
- Google Chrome
- Flask (Python package)
- spaCy (Python package)
- `en_core_web_sm` spaCy model
- Chrome Developer mode to load the extension

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your_username/email-summarizer.git
    cd email-summarizer
    ```

2. **Set up the Flask API**:

    Install the required Python packages:
    ```bash
    pip install Flask flask-cors spacy
    python -m spacy download en_core_web_sm
    ```

3. **Run the Flask API**:
    ```bash
    python email_summarizer_api.py
    ```

4. **Set up the Chrome Extension**:
    - Open Chrome and go to `chrome://extensions/`.
    - Enable **Developer mode** in the top-right corner.
    - Click **Load unpacked** and select the `email-summarizer` folder.
    - The extension should now be available in your Chrome browser.

## Usage
1. Open Gmail and view an email thread.
2. Click on the **Email Summarizer** Chrome extension.
3. Click the **Summarize Email** button to extract and summarize the email content.
4. The summary will be displayed in the extension popup.

## Troubleshooting
- If no summary appears, ensure that the Flask server is running and that the port number in `popup.js` matches the Flask server's port.
- If email content is not extracted correctly, check the selector in `content.js` to match Gmail's DOM structure.
