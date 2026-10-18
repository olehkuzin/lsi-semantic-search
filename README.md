# 🔍 LSI Search System  

A web application that enables **semantic document search** using **Latent Semantic Indexing (LSI)**. The system preprocesses text, computes **TF-IDF**, applies **Singular Value Decomposition (SVD)** for dimensionality reduction, and retrieves documents based on **cosine similarity**.  

---

## 🚀 Features  

- **Preprocessing**: Removes stopwords and applies stemming/lemmatization.  
- **TF-IDF Computation**: Converts documents into numerical vectors.  
- **SVD Decomposition**: Reduces dimensionality to enhance semantic search.  
- **Cosine Similarity**: Ranks documents by relevance to the search query.  
- **Flask API**: Handles search requests and retrieves relevant documents.  
- **React Frontend**: Provides a user-friendly interface for searching.  

---

## 📂 Project Structure  

📁 **vwm**  
│  
├── 📁 **backend**  
│   ├── `server.py`         # 🏗️ Flask backend API  
│   ├── `db.py`            # 🍃 MongoDB database connection  
│   ├── `preprocess.py`    # ✂️ Text preprocessing  
│   ├── `experiment.py`     # Experiments
│   ├── `TF-IDF.py`        # 🔢 TF-IDF computation  
│   ├── `SVD.py`           # 🔍 Singular Value Decomposition  
│   └── `cosineSimilarity.py` # 📐 Cosine similarity computation  
│  
├── 📁 **frontend**  
│   └── 📁 **src**  
│       ├── `pages/Home.js`  # 🔍 Search input and results display  
│       ├── `App.js`        # ⚛️ React app configuration  
│       ├── `pages/home.css`    # 🎨 Styling for UI
│       └── `App.css'`      # 🎨 Styling for UI
│  
├── `app.py`              # 🚀 Runs both frontend & backend  
└── `README.md`           # 📖 Project documentation  


---

## 🛠 Installation & Setup  

### **1️⃣ Clone the Repository**  
```bash
git clone git@gitlab.fit.cvut.cz:kuzinole/vwm.git
cd vwm
```

### 2️⃣ Setup Backend (Flask)
```bash
cd backend
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate virtual environment (Mac/Linux)
venv\bin\activate  # Activate virtual environment (Windows)
pip install -r requirements.txt  # Install dependencies
````
### 3️⃣ Setup Frontend (React)
```bash
cd ../frontend
rm -rf node_modules package-lock.json
npm cache clean --force
npm install
npm install --save-dev eslint-config-react-app eslint@latest
npm install eslint@^8.0.0 --save-dev
npm install eslint-config-react-app@latest --save-dev
npm start
````
### 4️⃣ Start the Project
```bash
cd ..
python app.py  # Runs both backend & frontend
```

## 🖥️ Technologies Used  

### **Backend**  
- 🐍 **Flask** – Web framework  
- 🍃 **MongoDB** – NoSQL database  
- ✂ **NLTK** – Text processing  
- 🔢 **Scikit-learn** – TF-IDF, SVD  

### **Frontend**  
- ⚛ **React** – UI framework  
- 🎨 **Tailwind CSS** – Styling  

## 🤝 Contributing  
Feel free to fork this repository and submit a pull request with improvements!  




