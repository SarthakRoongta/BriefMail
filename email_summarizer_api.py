
from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy

nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)
CORS(app)  

def summarize_text(text):
    doc = nlp(text)
    important_sentences = []
    for sent in doc.sents:
        if len(sent.ents) > 0:  
            important_sentences.append(sent.text)
    return " ".join(important_sentences)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    email_text = data.get('text')
        summary = summarize_text(email_text)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
