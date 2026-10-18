import os
from pymongo import MongoClient
import pandas as pd
import pickle

# MongoDB connection URI
MONGO_URI = os.environ["MONGO_URI"]

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["lsi_db"]
collection = db["lsi_search"]


def get_df():
    """
    Fetch documents from MongoDB and return them as a Pandas DataFrame.

    Returns:
    - DataFrame: Contains document details from MongoDB.
    """
    fields = {"_id": 1, "filename": 1, "category": 1, "title": 1, "content": 1}
    if "processed_content" in collection.find_one():
        fields["processed_content"] = 1
    documents = list(collection.find({}, fields))

    return pd.DataFrame(documents)


def update_df(df):
    """
    Update MongoDB collection with processed content.

    Parameters:
    - df (DataFrame): DataFrame containing document IDs and processed content.
    """
    for _, row in df.iterrows():
        collection.update_one(
            {"_id": row["_id"]},  # Locate document by ID
            {"$set": {"processed_content": row["processed_content"]}}  # Update processed content
        )


def save_doc_id():
    """
    Fetch document IDs from MongoDB and save them as a pickle file.

    Parameters:
    - file_path (str): Path to save the pickle file.
    """
    # Retrieve document IDs
    document_ids = [doc["_id"] for doc in collection.find({}, {"_id": 1})]

    # Save document IDs to a pickle file
    with open("../data/document_ids.pkl", "wb") as f:
        pickle.dump(document_ids, f)


def get_document_by_id(document_id):
    """
    Find a document in MongoDB by its _id and return its data as a DataFrame.

    Parameters:
    - document_id (str or ObjectId): The _id of the document to find.

    Returns:
    - DataFrame: Contains the document's data with columns ['_id', 'filename', 'category', 'title', 'content', 'processed_content'].
    """
    # Fetch the document from MongoDB
    document = collection.find_one({"_id": document_id})

    if document:
        # Convert the document to a DataFrame
        df = pd.DataFrame([document])
        return df
    else:
        # If no document is found, return an empty DataFrame with the required columns
        return pd.DataFrame(columns=['_id', 'filename', 'category', 'title', 'content', 'processed_content'])

