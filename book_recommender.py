import pandas as pd
import numpy as np
import streamlit as st

# ================================
# STEP 1: SET UP THE PAGE
# ================================

# This sets the title that appears at the top
st.title(" Book Recommendation System")



# These are download links to two files stored on Google Drive:
# - books_url: contains book info (ISBN number and book title)
# - ratings_url: contains ratings (which user rated which book, and what score they gave)
books_url = "https://drive.google.com/uc?export=download&id=1rEE9L2f5x0lovm9Xyd2_QgnJe4HuBLe-"
ratings_url = "https://drive.google.com/uc?export=download&id=13bCAwIpp61k41IwjAGV00MVEnXzgqNJx"

@st.cache_data

def load_data():
    # load files
    books = pd.read_csv(books_url, sep=';', encoding='latin-1', on_bad_lines='skip')
    ratings = pd.read_csv(ratings_url, sep=';', encoding='latin-1', on_bad_lines='skip')

    # keep needed columns
    books = books[['ISBN', 'Book-Title']]
    books['Book-Title'] = books['Book-Title'].str.lower().str.strip()

    # merge
    data = ratings.merge(books, on='ISBN')
    data = data.drop_duplicates(['User-ID', 'Book-Title'])

    # filter users
    user_counts = data['User-ID'].value_counts()
    active_users = user_counts[user_counts >= 10].index
    data = data[data['User-ID'].isin(active_users)]

    # filter books 
    book_counts = data['Book-Title'].value_counts()
    popular_books = book_counts[book_counts >= 100].index
    data = data[data['Book-Title'].isin(popular_books)]

    # pivot
    pivot = data.pivot_table(index='User-ID', columns='Book-Title', values='Book-Rating')
    pivot = pivot.fillna(0)

    return pivot
