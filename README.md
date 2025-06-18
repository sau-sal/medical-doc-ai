# Medical Document AI Extractor 🧾🧠

This project uses React (frontend) and FastAPI with Python (backend) to extract patient details like name, date, hospital, and billing amount from scanned medical documents.

## 🔍 Features
- Upload scanned PDF/image medical bills
- OCR + NLP-powered text extraction
- AI parses name, date, hospital, and amount
- View structured data on the UI

## 🛠️ Stack
- React.js (Frontend)
- FastAPI + Python (Backend)
- Tesseract OCR, spaCy NLP

## 📦 Run Locally
### 1. Backend
```bash
cd server
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

