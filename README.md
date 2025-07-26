# 🎬 Movie Recommendation System
This project implements a content-based movie recommendation system using TF-IDF, PCA, and cosine similarity. It suggests similar movies based on metadata such as genres, production companies, countries, languages, and movie overviews.


## 📌 Features

- **Content-based filtering** (no user ratings required).
- **Uses TF-IDF vectorization** on textual metadata.
- **Combines numeric features** like popularity and ratings.
- **Dimensionality reduction using PCA** for better performance.
- **Recommends the Top 10 similar movies** based on cosine similarity.

## 📂 Dataset

The project uses the **[Kaggle Movies Metadata dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)**.

## 📜 Step-by-Step Overview

### **1. Data Extraction and Loading**
- The movie dataset (CSV) is extracted from a ZIP file.
- Loaded into a pandas DataFrame `data`.
- `data.head(1)` is used to preview the structure of the dataset.

---

### **2. Data Cleaning**
- **Unnecessary columns dropped:** Columns like `homepage`, `title`, `budget`, etc., which are not relevant for the recommendation system, are removed using `drop()`.
- **Missing values handled:**
  - `NaN` values in key columns (`runtime`, `vote_count`, etc.) are removed using `dropna()`.
  - Missing values in the `overview` column are filled with `'Unknown'`.

---

### **3. Parsing JSON-like Columns**
- Columns such as `genres`, `spoken_languages`, `production_companies`, and `production_countries` are stored as stringified lists of dictionaries.
- `ast.literal_eval()` is used to safely convert these strings back into Python objects (lists/dictionaries).
- Each column is then processed to extract only the **`name`** field into a list of strings.

---

### **4. Text Preprocessing**
- For columns like `genres`, `production_companies`, etc., the list of strings is joined into a single space-separated string.  
  **Example:** `['Action', 'Adventure'] → "Action Adventure"`.

---

### **5. Text Vectorization (TF-IDF)**
- `TfidfVectorizer` converts the textual features into a numerical matrix by assigning higher weights to unique words in each movie description (`overview`) or other text columns.
- Combined text is created by merging all text columns (`genres`, `overview`, `production_companies`, etc.) into one string per row:
  ```python
  data['combined_text'] = [
      ' '.join(str(data[col].iloc[i]) for col in l) 
      for i in range(len(df))
  ]
  ```
- The TF-IDF matrix shape is (n_movies, n_features) (e.g., 45,000 movies × 500 features).

### **6. Numeric Features**
- Numeric columns like popularity, runtime, vote_average, vote_count are converted into a NumPy array.
- Combined matrix = [TF-IDF features + numeric columns].

### **7. Dimensionality Reduction (PCA)**
- PCA (Principal Component Analysis) is applied to reduce the high-dimensional feature matrix into fewer components (e.g., 100 dimensions).
- This speeds up similarity calculations and removes noise.

### **8. Cosine Similarity**
- A cosine similarity matrix is computed from the reduced PCA features.
--  The result is a square matrix (n_movies, n_movies) where each entry [i, j] is the similarity score between movie i and j.

### **9. Recommendation Logic**
- Given a movie name, find its index:
  ```python
  python
  Copy
  Edit
  ```
- Extract similarity scores for that movie from the similarity matrix.
- Sort movies by similarity score (descending) and select the Top 10 most similar movies.

### **10. Output Recommendations**
- Extract titles of the top 10 recommended movies:
```python
  python
  Copy
  Edit
  ```

## Key Points to Explain in Interview
- TF-IDF: Converts text into numerical vectors representing the importance of words.
- PCA: Reduces dimensionality to improve efficiency and remove noise.
- Cosine Similarity: Measures how similar two movies are based on their vectorized features.
- Hybrid Approach: Combines both textual data (overview, genres) and numeric data (popularity, ratings).
- End-to-End Workflow: Data cleaning → Feature engineering → Vectorization → Dimensionality reduction → Similarity → Top-N recommendations.










