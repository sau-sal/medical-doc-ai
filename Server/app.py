from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "no file uploaded"}), 400
    
    # Simulate AI processing
    result = {
        "status": "success",
        "extracted": {
            "patient_name": "John doe",
            "diagnosis": "Hypertension",
            "medications": ["Amlodipine", "Lisinopril"]
        }
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)