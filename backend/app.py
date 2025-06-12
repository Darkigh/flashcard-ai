import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import pdfplumber
import docx
from werkzeug.utils import secure_filename
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join([page.extract_text() or "" for page in pdf.pages])
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return ""

def generate_flashcards(text):
    prompt = (
        "Extract key facts from the following text as flashcards. "
        "Each flashcard should be a question and its answer. Return as a JSON list like: "
        "[{\"question\": \"...\", \"answer\": \"...\"}]\n\n"
        f"Text:\n{text[:4000]}"  # Truncate to fit token limits
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    try:
        return eval(response['choices'][0]['message']['content'])
    except Exception as e:
        return []

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    text = extract_text(filepath)
    if not text.strip():
        return jsonify({"error": "Could not extract text"}), 500

    flashcards = generate_flashcards(text)
    return jsonify({"flashcards": flashcards})

if __name__ == '__main__':
    app.run(debug=True)
