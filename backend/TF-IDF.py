"""
TF-IDF Matrix Generator

This script preprocesses textual data, computes TF-IDF values for the corpus,
and saves both the matrix and vectorizer for later use.

The TF-IDF model is used to convert text documents into numerical representations
that capture term importance for the LSI search model.
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import db
import pickle

df = db.get_df()

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()
# Transform the processed_content into a TF-IDF matrix
A = vectorizer.fit_transform(df["processed_content"])

"""
A stores nonzero values, reducing memory usage.

Example of A:
 (0, 24401)	0.12204012294089758
 (0, 4290)	0.356696552426836

where 
Row 0 → First document.
Column 24401 → This is a specific word (term).
Value 0.1220 → This is the TF-IDF weight for that word in the first document.
"""

# Get feature names (terms/words)
terms = vectorizer.get_feature_names_out()
# Convert to DataFrame where columns are terms/words and rows are documents
tfidf_df = pd.DataFrame(A.toarray(), columns=terms)

# Save the TF-IDF matrix to a pickle file
with open("../data/tfidf_matrix.pkl", "wb") as f:
    pickle.dump(A, f)

# Save the TF-IDF vectorizer to a pickle file
with open("../data/tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# To Load the TF-IDF matrix from the pickle file use the following code:
# with open("../tfidf_matrix.pkl", "rb") as f:
#     A = pickle.load(f)
