from flask import Flask, request, jsonify
from pytesseract import image_to_string
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
from PIL import Image
import spacy
import os
from werkzeug.utils import secure_filename

# Flask-App initialisieren
app = Flask(__name__)

# SpaCy-Modell laden
nlp = spacy.load("en_core_web_sm")

def extract_text_from_image(file):
    """OCR für ein Bild ausführen."""
    # Temporäre Datei speichern
    temp_filename = secure_filename(file.filename)
    temp_path = os.path.join("/tmp", temp_filename)  # Temporärverzeichnis verwenden
    file.save(temp_path)

    # Bild laden und OCR ausführen
    image = Image.open(temp_path)
    text = image_to_string(image)

    # Temporäre Datei löschen
    os.remove(temp_path)
    return text

def extract_text_from_pdf(file):
    """Versuche, Text direkt aus PDF zu extrahieren; falls nicht möglich, nutze OCR."""
    # Temporäre Datei speichern
    temp_filename = secure_filename(file.filename)
    temp_path = os.path.join("/tmp", temp_filename)
    file.save(temp_path)

    try:
        # Versuch, Text direkt mit PyPDF2 zu extrahieren
        reader = PdfReader(temp_path)
        text = "".join(page.extract_text() for page in reader.pages if page.extract_text())
        if text.strip():  # Wenn Text gefunden wurde, zurückgeben
            os.remove(temp_path)
            return text
    except Exception as e:
        print(f"Fehler beim direkten Extrahieren: {e}")

    # Fallback: OCR verwenden
    images = convert_from_path(temp_path)
    text = ""
    for image in images:
        text += image_to_string(image)

    os.remove(temp_path)
    return text

def anonymize_text(text):
    """Selektive PII-Anonymisierung mit SpaCy."""
    doc = nlp(text)
    anonymized_text = text

    # Kategorien, die anonymisiert werden sollen
    sensitive_entities = ["PERSON", "GPE", "ORG", "DATE"]

    for ent in doc.ents:
        if ent.label_ in sensitive_entities:
            # Nur sensible Informationen anonymisieren
            anonymized_text = anonymized_text.replace(ent.text, "[ANONYMIZED]")
    
    return anonymized_text

@app.route('/process', methods=['POST'])
def process_file():
    """Datei verarbeiten (OCR + Anonymisierung)."""
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files['file']
    
    if file.filename.endswith('.pdf'):
        text = extract_text_from_pdf(file)
    else:
        image = Image.open(file)
        text = extract_text_from_image(image)
    
    anonymized_text = anonymize_text(text)
    
    return jsonify({"original_text": text, "anonymized_text": anonymized_text})

if __name__ == "__main__":
    app.run(debug=True)
