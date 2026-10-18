import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import db

# Download required NLTK resources
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")


def preprocess_text(text):
    """
    Clean and preprocess text:
    - Convert to lowercase
    - Remove non-alphanumeric characters
    - Tokenize
    - Remove stopwords
    - Lemmatize words
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)  # Keep spaces for proper tokenization
    tokens = word_tokenize(text)

    # Filter out stopwords
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stopwords.words("english")]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return " ".join(tokens)


# Load documents from database
df = db.get_df()

# Apply text preprocessing to the 'content' column
df["processed_content"] = df["content"].apply(preprocess_text)

# Update the database with processed content
db.update_df(df)

print("Database successfully updated with preprocessed text!")
