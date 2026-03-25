# 📚 Book Recommendation System

A web app that recommends books based on what similar users have rated. Built with Python and Streamlit, using a real-world dataset of 1 million book ratings.

---

## What Does It Do?

You pick a book from a dropdown, click **Recommend**, and the app gives you 5 books that readers with similar taste also enjoyed.

It does not use genres or descriptions — it works purely on **user behaviour**. If many users who rated Book A also rated Book B highly, the app considers them similar.

---

## How to Set It Up

### 1. Make sure Python is installed
You can check by running:
```bash
python --version
```
If you don't have it, download it from [python.org](https://python.org).

### 2. Install the required libraries
```bash
pip install streamlit pandas numpy
```

### 3. Download the project file
Save `book_recommender.py` into a folder on your computer.

### 4. Run the app
```bash
streamlit run book_recommender.py
```

The app will open automatically in your browser. If it doesn't, go to `http://localhost:8501`.

> The first load takes a minute — it's downloading and processing the dataset from Google Drive.

---

## How to Use It

1. Wait for the data to finish loading (you'll see a spinner)
2. Use the dropdown to select a book
3. Click the **Recommend** button
4. The app displays 5 recommended books

---

## How It Works

### Data
The app uses two files from the [Book-Crossing dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/):
- `Books.csv` — book titles and ISBNs
- `Ratings.csv` — user ratings (scale of 1–10)

### Filtering
Before making recommendations, the data is filtered to improve quality:
- Only users who rated **10 or more** books are kept
- Only books rated by **100 or more** users are kept

This removes noise from users who barely interacted with the platform and books with too little data.

### Recommendation — L2 Norm (Euclidean Distance)
Each book is represented as a **vector** — a list of ratings given by every user. To find similar books, the app calculates the **Euclidean distance** (also called the L2 norm) between two book vectors:

```
distance = sqrt( sum of (a - b)^2 )
```

Where `a` and `b` are the rating vectors of two books. A small distance means users rated both books similarly, making them a good recommendation match.

In code:
```python
distance = np.sqrt(np.sum((selected_book_ratings - other_book_ratings) ** 2))
```

The 5 books with the smallest distance are returned as recommendations.

---

## Project Structure

```
book-recommendation/
│
├── book_recommender.py   # Main application
└── README.md             # This file
```

---

## Libraries Used

| Library | Purpose |
|---|---|
| `streamlit` | Builds the web interface |
| `pandas` | Loads and processes the CSV data |
| `numpy` | Calculates Euclidean distance |
