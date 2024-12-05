import streamlit as st
import requests
import os

# Flask-Backend-URL
BACKEND_URL = "http://127.0.0.1:5000/process"

# Streamlit-Anwendung
st.title("KI-gestützte Text-Extraktion und Anonymisierung")
st.markdown("Lade ein Dokument hoch (Bild oder PDF), um Text zu extrahieren und anonymisieren zu lassen.")

# Datei-Upload
uploaded_file = st.file_uploader("Ziehe Dateien hier rein oder klicke, um hochzuladen", type=["png", "jpg", "jpeg", "pdf"])

if uploaded_file is not None:
    with st.spinner("Verarbeite die Datei..."):
        # Datei an Backend senden
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        try:
            response = requests.post(BACKEND_URL, files=files)
            response.raise_for_status()  # Raise error for bad status codes
            result = response.json()
            
            # Ergebnisse anzeigen
            st.subheader("Originaltext")
            st.text_area("Extrahierter Text", result["original_text"], height=300)

            st.subheader("Anonymisierter Text")
            st.text_area("Anonymisierter Text", result["anonymized_text"], height=300)
        except requests.exceptions.RequestException as e:
            st.error(f"Fehler beim Verarbeiten der Datei: {e}")
