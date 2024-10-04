import nltk
import os

# Define the path to save the NLTK data
nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')

# If the directory does not exist, create it
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)

# Add this folder to NLTK's search path
nltk.data.path.append(nltk_data_path)

git add legal_document_nlp/
# Download the necessary resources to this folder
nltk.download('punkt', download_dir=nltk_data_path)

import PyPDF2
import spacy
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

# Load Spacy's pre-trained model
nlp = spacy.load('en_core_web_sm')

# Function to load and extract text from a PDF
def load_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in range(len(reader.pages)):
                text += reader.pages[page].extract_text()
        print("\nPDF loaded successfully!")
        return text
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None

# Function to summarize the document
def summarize_text(text):
    if text is None or text.strip() == "":
        return "No text to summarize."
    
    # Use Spacy to process the document
    doc = nlp(text)
    
    # Extract sentences from the document using NLTK
    sentences = sent_tokenize(text)
    
    # Rank sentences by length or importance (for simplicity, we take the first 5 sentences)
    summary = ' '.join(sentences[:5]) if len(sentences) > 5 else text
    
    return summary

# Main function
def main():
    # Load legal document (Change the file path to your legal document PDF)
    file_path = 'legal.pdf'
    
    legal = load_pdf(file_path)
    
    # Check if any text was extracted
    if legal:
        print("\n=== Extracted Text from PDF ===\n")
        print(legal[:1000])  # Print the first 1000 characters to verify the text was extracted

        # Summarize the legal document
        summary = summarize_text(legal)

        # Output the summary
        print("\n=== Legal Document Summary ===\n")
        print(summary)
    else:
        print("Failed to extract text from PDF.")

if __name__ == "__main__":
    main()
