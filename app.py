from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_ENDPOINT = "END-POINT-URL"  # Replace with your endpoint
BEARER_TOKEN = "BEARER_TOKEN"  # Replace with your actual bearer token

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_message = request.form.get("user_message")

        payload = {
                    "shandover": {
                    "user_id": 3593,
                    "user_name": "Thanura Manjitha Peiris",
                    "message": {
                        "message": user_message,
                        "file_url": "null",
                        "mime_type": "null",
                        "type": "text"
                    },
                    "past_message": False,
                    "model": "gemini-2.0-flash",
                    "actt_flow": {
                        "geminiSystemPrompt": "geminiSystemPrompt",
                        "embedding_model": "text-embedding-3-large",
                        "dimensions": 3072,
                        "modelVersion": "gemini-2.0-flash",
                        "imageModelVersion": "gemini-2.0-flash",
                        "languageDetectionModelVersion": "gemini-2.0-flash",
                        "keywordModelVersion": "gemini-2.0-flash",
                        "conversationModelVersion": "gemini-2.0-flash",
                        "indexes": [
                            "oleon-for-fintrex-new"
                        ],
                        "pinecone_api_key": "PINECONE-API",
                        "pinecone_region": "us-east-1",
                        "productKeywordSystemPrompt": "productKeywordSystemPrompt"
                    }
                },
                "encrypt": False
        }

        headers = {
            "Authorization": f"Bearer {BEARER_TOKEN}",
            "Content-Type": "application/json"
        }

        try:
            res = requests.post(API_ENDPOINT, json=payload, headers=headers)
            res_json = res.json()
            

            answer = res_json.get("answer", "No answer provided.")
            language = res_json.get("processingInfo", {}).get("languageDetected", "Unknown")
            chunks = res_json.get("relevantChunks", [])

            return render_template("index.html", answer=answer, language=language, chunks=chunks, message=user_message)
        except Exception as e:
            return render_template("index.html", error=str(e), message=user_message)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
