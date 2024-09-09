
# How to Run the Email Summarizer Extension

### Step 1: Install Dependencies

1. Install Python 3.x if you don't have it installed already.
2. Install the necessary Python packages:
    ```bash
    pip install Flask flask-cors spacy
    python -m spacy download en_core_web_sm
    ```

### Step 2: Start the Flask API

1. Navigate to the directory where `email_summarizer_api.py` is located.
2. Start the Flask server:
    ```bash
    python email_summarizer_api.py
    ```
3. The Flask API will now be running on `http://localhost:5001` (or another port if configured).

### Step 3: Load the Chrome Extension

1. Open Chrome and navigate to `chrome://extensions/`.
2. Enable **Developer mode**.
3. Click **Load unpacked** and select the folder containing the extension files.
4. The extension will appear in your browser's toolbar.

### Step 4: Use the Extension

1. Open Gmail and view an email thread.
2. Click the **Email Summarizer** extension icon.
3. Click **Summarize Email** to extract and summarize the email thread content.

### Notes

- If you're using a different port for the Flask API, be sure to update the URL in `popup.js`.
