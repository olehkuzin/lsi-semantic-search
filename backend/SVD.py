"""
This script performs Singular Value Decomposition (SVD) on the TF-IDF matrix.
SVD is a dimensionality reduction technique that is used to reduce the number of features in the data.
"""
from sklearn.decomposition import TruncatedSVD
import pickle

# Load A matrix from pickle file
with open("../data/tfidf_matrix.pkl", "rb") as f:
    A = pickle.load(f)

# Perform SVD on the TF-IDF matrix
svd = TruncatedSVD(n_components=200, random_state=42)
A_reduced = svd.fit_transform(A)

"""
A_reduced stores the reduced matrix after SVD.
After applying SVD, the matrix no longer contains individual words, but instead latent topics.
The number of components (n_components) is a hyperparameter that can be tuned.
Latent Topics are abstract concepts or themes that represent relationships between words.
Each document is now represented by a combination of these topics, rather than individual word frequencies.
Instead of saying "this document contains 'AI', 'machine learning', 'data'", we now say "this document is 80% 
about Topic_1 and 20% about Topic_2".
"""

# Save the A_reduce matrix to a pickle file
with open("../data/svd_matrix.pkl", "wb") as f:
    pickle.dump(A_reduced, f)

# Save the SVD model to a pickle file
with open("../data/svd_model.pkl", "wb") as f:
    pickle.dump(svd, f)
