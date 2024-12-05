# 🏥 **Projekt: KI-gestützte Text-Extraktion und Anonymisierung**

## 📝 **Einleitung**
Dieses Projekt dient der Extraktion von Text aus medizinischen Dokumenten wie Arztbriefen oder radiologischen Befunden. Die extrahierten Informationen werden zusätzlich anonymisiert, um sensible Daten wie Namen, Adressen oder Geburtsdaten zu schützen. Die Anwendung besteht aus einem Backend (Flask) und einem Frontend (Streamlit), die in Docker-Containern laufen.

---

## 🔍 **Was ist OCR?**
OCR (Optical Character Recognition) ist eine Technologie, die gedruckten oder handgeschriebenen Text aus Bildern, PDFs oder anderen Dokumenten erkennt und in maschinenlesbaren Text umwandelt. 

- **Beispiel:** Ein gescannter Arztbrief enthält möglicherweise Text als Bild. OCR erkennt diesen Text und konvertiert ihn in editierbaren Text.
- **Warum wichtig?** OCR ermöglicht die Digitalisierung von Papierdokumenten und macht sie durchsuchbar, analysierbar und leicht verarbeitbar.

---

## 📁 **Projektstruktur**
```
project/
├── docker-compose.yml    # Docker-Compose Datei für das Projekt
├── backend/              # Flask-Backend für OCR und Anonymisierung
│   ├── Dockerfile
│   ├── app.py            # Haupt-Backend-Skript
│   ├── requirements.txt  # Python-Abhängigkeiten für das Backend
└── frontend/             # Streamlit-Frontend zur Interaktion mit der Anwendung
    ├── Dockerfile
    ├── frontend.py       # Haupt-Frontend-Skript
    ├── requirements.txt  # Python-Abhängigkeiten für das Frontend
```

---

## ⚙️ **Voraussetzungen**
- Installiertes **Docker** und **Docker Compose**
- Optional: **Python 3.10+** (falls das Projekt ohne Docker ausgeführt wird)

---

## 🚀 **Wie startet man das Projekt?**

### 1. **Clone das Projekt**
Lade das Projekt von GitHub oder einer anderen Quelle herunter:
```bash
git clone https://github.com/username/medical-information-poc.git
cd medical-information-poc
```

### 2. **Starte die Anwendung mit Docker Compose**
Baue und starte die Anwendung:
```bash
docker-compose up --build
```

### 3. **Zugriff auf die Anwendung**
- **Frontend (Streamlit)**: [http://localhost:8501](http://localhost:8501)
- **Backend (Flask)**: [http://localhost:5000](http://localhost:5000)

---

## 💡 **Wie funktioniert die Anwendung?**

### **Frontend (Streamlit):**
- Benutzer können Dateien wie PDFs oder Bilder in die Anwendung ziehen.
- Das Frontend sendet die Dateien an das Backend zur Verarbeitung.
- Nach Abschluss der Verarbeitung werden die extrahierten und anonymisierten Texte angezeigt.

### **Backend (Flask):**
- **OCR-Verarbeitung**:
  1. PDF-Dateien:
     - Enthält die Datei eingebetteten Text, wird dieser direkt extrahiert.
     - Enthält die Datei nur gescannte Bilder, werden die Seiten in Bilder umgewandelt, und OCR wird angewendet.
  2. Bilddateien:
     - Bilder werden direkt mit OCR analysiert.
- **Anonymisierung**:
  - Sensible Informationen wie Namen, Adressen oder Geburtsdaten werden durch "[ANONYMIZED]" ersetzt, während medizinische Diagnosen und Fachbegriffe erhalten bleiben.

---

## 🔧 **Technischer Überblick (vereinfacht für Laien)**
1. **OCR-Technologie:**
   - Identifiziert Buchstaben und Wörter aus hochgeladenen Bildern oder PDFs.
   - Beispiel: Aus einem gescannten Arztbrief mit "Herr Max Beispiel" wird der Text "Herr Max Beispiel" extrahiert.

2. **Anonymisierung:**
   - Durch Künstliche Intelligenz erkennt die Anwendung persönliche Daten (z. B. Namen, Adressen) und ersetzt sie durch Platzhalter.

3. **Docker-Container:**
   - Jeder Teil der Anwendung (Backend und Frontend) läuft in einer isolierten Umgebung. Das macht die Anwendung portabel und einfach zu starten.

---

## ❓ **FAQ**

1. **Was passiert mit meinen Daten?**
   - Die Daten werden nur lokal verarbeitet. Es gibt keinen Upload in die Cloud.

2. **Was, wenn keine Anonymisierung nötig ist?**
   - Du kannst die Anonymisierungsfunktion deaktivieren, indem du den entsprechenden Code im Backend auskommentierst.

3. **Warum wird die Diagnose manchmal anonymisiert?**
   - Falls die Diagnose versehentlich anonymisiert wird, überprüfe die Anpassung der Anonymisierungslogik im Backend.

---

## 🔄 **Verbesserungsmöglichkeiten**
- Hinzufügen weiterer Sprachen für die OCR-Verarbeitung.
- Bessere Erkennung medizinischer Fachbegriffe durch spezialisierte Modelle.
- Optimierung des Frontends für eine benutzerfreundlichere Oberfläche.

---

## 🛠️ **Fehlerbehebung**
- **Docker startet nicht:**
  - Stelle sicher, dass Docker und Docker Compose installiert sind und laufen.
- **Flask-Backend gibt 500-Fehler zurück:**
  - Prüfe, ob alle benötigten Python-Bibliotheken installiert sind.
  - Überprüfe die Dateiwege im Code.

---

Viel Erfolg mit der Anwendung! 🚀
