# Book Recommendation System

A web application that recommends books based on the preferences of similar users. Built using Python and Streamlit, the system uses a real-world dataset containing over one million user ratings.

---

## Live Demo

You can try the application without installing anything:

https://bookrecommendationsystem-nnlxfhtmzesp58n2pygjfx.streamlit.app/

---

## What Does It Do?

The application allows users to select a book from a dropdown menu and receive five recommendations based on similar user preferences.

The system does not rely on genres, descriptions, or metadata. Instead, it uses collaborative filtering based entirely on user behavior. If multiple users who liked one book also liked another, those books are considered similar.

---

## How to Run Locally

### 1. Install Python

Check if Python is installed:

```bash
python --version
```

If not installed, download it from: https://python.org

---

### 2. Install Required Libraries

```bash
pip install streamlit pandas numpy
```

---

### 3. Download the Project File

Save the file `book_recommender.py` in a folder on your system.

---

### 4. Open Command Prompt in the Project Folder

It is important to run the command from the same folder where the Python file is located.

Steps:
- Open the folder containing `book_recommender.py`
- Click on the address bar
- Type `cmd` and press Enter

---

### 5. Run the Application

```bash
python -m streamlit run book_recommender.py
```

The application will open in your default browser.  
If it does not open automatically, go to:

http://localhost:8501

Note: The first run may take some time as the dataset is downloaded and processed.

---

## How to Use

1. Wait for the dataset to load  
2. Select a book from the dropdown menu  
3. Click the "Recommend" button  
4. View the recommended books  

---

## How It Works

### Dataset

The application uses the following files from the Kaggle Book Recommendation dataset:

- `BX-Books.csv` — Contains book titles and ISBNs  
- `BX-Book-Ratings.csv` — Contains user ratings on a scale of 1 to 10  

Dataset link: https://www.kaggle.com/datasets/ra4u12/bookrecommendation

---

### Data Filtering

To improve recommendation quality, the dataset is filtered as follows:

- Only users who have rated at least 10 books are considered  
- Only books that have received at least 100 ratings are included  

This reduces noise and ensures meaningful similarity comparisons.

---

### Recommendation Method (L2 Norm / Euclidean Distance)

Each book is represented as a vector of user ratings. Similarity between books is computed using Euclidean distance (L2 norm).

Formula:

```
distance = sqrt( sum of (a - b)^2 )
```

Where `a` and `b` are rating vectors of two books.

Implementation:

```python
distance = np.sqrt(np.sum((selected_book_ratings - other_book_ratings) ** 2))
```

Books with the smallest distance are considered most similar and are recommended to the user.

---

## Project Structure

```
book-recommendation/
│
├── book_recommender.py   # Main application
└── README.md             # Documentation
```

---

## Libraries Used

| Library   | Purpose                          |
|-----------|----------------------------------|
| streamlit | Web application interface        |
| pandas    | Data loading and processing      |
| numpy     | Numerical computation            |

---

## Summary

This project demonstrates a collaborative filtering-based recommendation system using a user-item interaction matrix and Euclidean distance. It highlights how meaningful recommendations can be generated purely from user behavior without relying on additional metadata.
