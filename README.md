# LSI Semantic Search

A web application for **semantic document search** using **Latent Semantic Indexing (LSI)**.
Documents are preprocessed (stopword removal, WordNet lemmatization), turned into **TF-IDF**
vectors, and reduced with **truncated SVD**. Queries are ranked by **cosine similarity** in the
reduced space. A Flask API serves the search, and a React frontend provides the UI.
The corpus is the BBC News articles dataset, stored in MongoDB.

Team project for the VWM course at FIT ČVUT (Czech Technical University in Prague), 2025,
by Oleh Kuzin and Andrii Kozlov. The written report is in
[`docs/LSI_vector_model_report.pdf`](docs/LSI_vector_model_report.pdf).

## Tech stack

- **Backend:** Python, Flask, flask-cors, pymongo, NLTK, scikit-learn, pandas, NumPy
- **Database:** MongoDB (Atlas or local)
- **Frontend:** React (Create React App)

## Project structure

```
backend/
  server.py             Flask API (POST /search)
  db.py                 MongoDB access (reads MONGO_URI from the environment)
  preprocess.py         Text preprocessing, writes processed_content back to MongoDB
  TF-IDF.py             Builds the TF-IDF matrix and vectorizer (data/*.pkl)
  SVD.py                Truncated SVD of the TF-IDF matrix (data/svd_*.pkl)
  cosineSimilarity.py   Query projection and ranking
  experiment_k.py       Compares results for different SVD dimensions k
frontend/               React UI (src/pages/Home.js calls http://127.0.0.1:5000/search)
scripts/
  transform_script.py   Converts the BBC News text files into scripts/data.json
docs/                   Project report
app.py                  Starts the backend and the frontend together
```

## Setup

### 1. Configuration

```bash
cp .env.example .env      # then fill in your MongoDB connection string
set -a; source .env; set +a
```

`backend/db.py` reads the `MONGO_URI` environment variable and uses the database `lsi_db`,
collection `lsi_search`.

### 2. Backend

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Frontend

```bash
cd frontend
npm install
```

## Data

**Not included:** the BBC News dataset (`data/BBC News Articles/<category>/*.txt`), the
generated `scripts/data.json`, and the generated model pickles in `data/`. To rebuild them:

1. Put the BBC News articles in `data/BBC News Articles/`, one folder per category.
2. `cd scripts && python transform_script.py` creates `scripts/data.json`.
3. Import `data.json` into MongoDB (`lsi_db.lsi_search`). The repository has no import
   script, so use a tool such as `mongoimport --jsonArray`.
4. From `backend/`:
   - `python preprocess.py` stores the preprocessed text in MongoDB.
   - `python TF-IDF.py`
   - `python SVD.py`
   - Run `db.save_doc_id()` once (e.g. `python -c "import db; db.save_doc_id()"`) to create `data/document_ids.pkl`.

## Usage

```bash
python app.py
```

This starts the Flask server (port 5000) and then the React dev server (`npm start`).

## Screenshots

<!-- TODO: add a screenshot of the search UI -->

## License

[MIT](LICENSE). The BBC News dataset is not part of this repository and is not covered by
this license.
