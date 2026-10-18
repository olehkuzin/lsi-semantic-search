import pickle
import numpy as np


def compute_cosine_similarity(vector_a, vector_b):
    """
    Compute the cosine similarity between two vectors.

    Parameters:
    - vector_a (numpy array): First vector.
    - vector_b (numpy array): Second vector.

    Returns:
    - float: Cosine similarity score.
    """
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)

    return 0 if norm_a == 0 or norm_b == 0 else dot_product / (norm_a * norm_b)


def compute_all_similarities(query_vector, document_matrix):
    """
    Compute cosine similarity between the query vector and all document vectors.

    Parameters:
    - query_vector (numpy array): Query representation in the reduced SVD space.
    - document_matrix (numpy array): Matrix of all document vectors in the reduced SVD space.

    Returns:
    - numpy array: Array of similarity scores for each document.
    """
    return np.array([compute_cosine_similarity(query_vector, doc_vector) for doc_vector in document_matrix])


def search_documents(query, tfidf_vectorizer, svd_model, reduced_matrix, document_ids, top_n=5):
    """
    Perform document retrieval based on cosine similarity in the reduced SVD space.

    Parameters:
    - query (str): The search query.
    - tfidf_vectorizer (TfidfVectorizer): Pre-trained TF-IDF vectorizer.
    - svd_model (TruncatedSVD): Pre-trained SVD model.
    - reduced_matrix (numpy array): Reduced document-term matrix after SVD.
    - document_ids (list): List of document IDs corresponding to rows in the reduced_matrix.
    - top_n (int): Number of top results to return.

    Returns:
    - list of tuples (document_id, similarity_score): Top-N most relevant documents.
    """
    # Transform the query into the TF-IDF space
    query_tfidf = tfidf_vectorizer.transform([query])

    # Transform the query into the reduced SVD space
    query_svd = svd_model.transform(query_tfidf)

    # Compute cosine similarity between query and all documents
    similarity_scores = compute_all_similarities(query_svd, reduced_matrix).flatten()

    # Get indices of top-N most similar documents
    top_indices = np.argsort(similarity_scores)[-top_n:][::-1]

    # Return the most similar documents along with their similarity scores
    return [(document_ids[i], similarity_scores[i]) for i in top_indices]


def load_model(file_path):
    """
    Load a model or matrix from a pickle file.

    Parameters:
    - file_path (str): Path to the pickle file.

    Returns:
    - object: Loaded model or matrix.
    """
    with open(file_path, "rb") as f:
        return pickle.load(f)

