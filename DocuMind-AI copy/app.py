from flask import Flask, render_template, request, jsonify
from rag.document_processor import DocumentProcessor
from rag.rag_pipeline import RAGPipeline
import os

app = Flask(__name__)

# Initialize document processor
processor = DocumentProcessor()

# Do NOT initialize pipeline at startup.
# It will be created only after a PDF is uploaded.
pipeline = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    global pipeline

    if "pdf" not in request.files:
        return jsonify({
            "status": "error",
            "message": "No PDF uploaded."
        }), 400

    file = request.files["pdf"]

    if file.filename == "":
        return jsonify({
            "status": "error",
            "message": "No file selected."
        }), 400

    os.makedirs("uploads", exist_ok=True)

    filepath = os.path.join(
        "uploads",
        file.filename
    )

    file.save(filepath)

    chunks = processor.process_pdf(filepath)

    # Now that vector_db exists,
    # create the pipeline.
    pipeline = RAGPipeline()

    return jsonify({
        "status": "success",
        "chunks": chunks
    })


@app.route("/ask", methods=["POST"])
def ask():

    global pipeline

    if pipeline is None:

        return jsonify({
            "answer": "Please upload a PDF first."
        })

    data = request.get_json()

    question = data.get("question", "").strip()

    if question == "":
        return jsonify({
            "answer": "Please enter a question."
        })

    answer = pipeline.ask(question)

    return jsonify({
        "answer": answer
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )