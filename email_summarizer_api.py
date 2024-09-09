
from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy

# Load spaCy's language model (or any other NLP model you prefer)
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

def summarize_text(text):
    # Process the email text with spaCy
    doc = nlp(text)

    # Extract the most important sentences (for simplicity, sentences with most named entities, etc.)
    important_sentences = []
    for sent in doc.sents:
        if len(sent.ents) > 0:  # Example: prioritize sentences with named entities
            important_sentences.append(sent.text)

    # Return summary as a string of the most important sentences
    return " ".join(important_sentences)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    email_text = data.get('text')
    
    # Summarize the email content
    summary = summarize_text(email_text)
    
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
