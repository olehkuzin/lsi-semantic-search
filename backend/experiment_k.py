import time
import pickle
from cosineSimilarity import search_documents
from db import get_document_by_id

# Load models and matrices
with open("../data/tfidf_vectorizer.pkl", "rb") as f:
    tfidf_vectorizer = pickle.load(f)

with open("../data/document_ids.pkl", "rb") as f:
    document_ids = pickle.load(f)

# Queries to test
queries = [
    ("football world cup", "sport"),
    ("artificial intelligence in medicine", "tech"),
    ("classical music theory", "music"),
    ("new car models 2024", "autos"),
    ("space exploration mars", "science"),
    ("benefits of meditation", "health"),
    ("brazilian carnival traditions", "culture"),
    ("machine learning algorithms", "tech"),
    ("piano composition techniques", "music"),
    ("world war II history", "history"),
    ("electric vehicles market growth", "autos"),
    ("covid-19 vaccine development", "health"),
    ("climate change effects", "science"),
    ("popular dog breeds", "animals"),
    ("deep learning in image recognition", "tech")
]

# Different k values to test
ks = [10, 50, 100, 150, 200, 300]

print("| Query | k | Relevant Matches | Time (s) |")
print("|-------|----|------------------|----------|")

best_config = None
best_score = -1
best_time = float('inf')

for k in ks:
    with open(f"../data/svd_model_k{k}.pkl", "rb") as f:
        svd_model = pickle.load(f)
    with open(f"../data/svd_matrix_k{k}.pkl", "rb") as f:
        reduced_matrix = pickle.load(f)

    total_matches = 0
    total_time = 0

    for query_text, expected_category in queries:
        start = time.time()
        results = search_documents(query_text, tfidf_vectorizer, svd_model, reduced_matrix, document_ids)
        duration = time.time() - start
        total_time += duration

        match_count = 0
        for doc_id, _ in results:
            df = get_document_by_id(doc_id)
            category = df['category'].iloc[0].lower()
            if expected_category in category:
                match_count += 1

        total_matches += match_count
        print(f"| {query_text} | {k} | {match_count}/5 | {duration:.2f} |")

    avg_time = total_time / len(queries)

    if (total_matches > best_score) or (total_matches == best_score and avg_time < best_time):
        best_config = k
        best_score = total_matches
        best_time = avg_time

print("\n✅ Best configuration:")
print(f"k = {best_config}, total relevant matches = {best_score}, average time = {best_time:.2f}s")