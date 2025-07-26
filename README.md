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

