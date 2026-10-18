import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from cosineSimilarity import search_documents, load_model
from db import get_document_by_id

app = Flask(__name__)
CORS(app)

# Get the absolute path of the "data" folder
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")

# Load models with absolute paths
tfidf_vectorizer = load_model(os.path.join(DATA_DIR, "tfidf_vectorizer.pkl"))
svd_model = load_model(os.path.join(DATA_DIR, "svd_model.pkl"))
reduced_matrix = load_model(os.path.join(DATA_DIR, "svd_matrix.pkl"))
document_ids = load_model(os.path.join(DATA_DIR, "document_ids.pkl"))


@app.route("/search", methods=["POST"])
def search():
    if request.method == "POST":
        data = request.json
        query = data.get("query", "")

        if not query:
            return jsonify({"error": "Empty query"}), 400

        # Perform document search
        search_results = search_documents(query, tfidf_vectorizer, svd_model, reduced_matrix, document_ids)

        # Convert the result into a JSON-compatible format
        formatted_results = []
        top_result = get_document_by_id(search_results[0][0])
        top_score = float(search_results[0][1])
        top_result_title = top_result['category'].iloc[0]
        top_result_content = top_result['content'].iloc[0]
        formatted_results.append({"tit": top_result_title, "con": top_result_content,
                                  "sc": int(top_score * 100), "quer": str(query)})

        search_by_top_result = search_documents(top_result_content, tfidf_vectorizer, svd_model, reduced_matrix, document_ids)

        for doc_id, score in search_by_top_result[1:]:
            df = get_document_by_id(doc_id)
            title = df['category'].iloc[0]  # Extract the first value from the Series
            content = df['content'].iloc[0]  # Extract the first value from the Series
            int_score = int(float(score) * 100)
            print("Document ID: " + str(doc_id) + ", Similarity score: " + str(score))
            formatted_results.append({"tit": title, "con": content, "sc": int_score, "quer": str(query)})

        # Return the JSON response
        if int(top_score * 100) == 0:
            empty_res = []
            empty_res.append({"tit": "empty", "con": "empty", "sc": 0, "quer" : str(query)})
            return jsonify({"results": empty_res})
        else:
            return jsonify({"results": formatted_results})

    return jsonify({"error": "Method not allowed"}), 405


if __name__ == "__main__":
    app.run(debug=True)
