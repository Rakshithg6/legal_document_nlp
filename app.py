from flask import Flask, render_template, request, redirect, url_for
import fitz  # PyMuPDF
from transformers import pipeline  # Hugging Face transformers for summarization

app = Flask(__name__)

# Summarizer using Hugging Face Transformers
summarizer = pipeline('summarization')

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling file upload and summarization
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    # Extract text from PDF
    if file and file.filename.endswith('.pdf'):
        doc = fitz.open(file.stream)
        text = ""
        for page in doc:
            text += page.get_text()

        # Perform summarization
        summary = summarizer(text, max_length=200, min_length=50, do_sample=False)

        return render_template('summary.html', summary=summary[0]['summary_text'])

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
