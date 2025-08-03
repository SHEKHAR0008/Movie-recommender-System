import streamlit as st
import pickle
import pandas as pd
import requests
# Load Data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
movies_list = movies['title'].values

similarity_movies = pickle.load(open('similarity.pkl', 'rb'))

books_dict = pickle.load(open('books_dict.pkl', 'rb'))
books = pd.DataFrame(books_dict)
books_list = books['title'].values

similarity_books = pickle.load(open('similarity_books.pkl', 'rb'))

# Functions
def recommend_movie(movie):
    movie_idx = movies[movies["title"] == movie].index[0]
    distances = similarity_movies[movie_idx]
    idx = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [(i[0], movies.iloc[i[0]]['title']) for i in idx]

def recommend_book(book):
    books_idx = books[books["title"] == book].index[0]
    distances = similarity_books[books_idx]
    idx = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_books = books.iloc[[i[0] for i in idx]]
    return list(zip(recommended_books['title'], recommended_books['thumbnail']))


# Page Layout
st.title("📚🎬 Recommender System")

tabs = st.tabs(["🎥 Movie Recommender", "📖 Book Recommender"])

def movie_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=da4979a119db5aaf28b05f4aee2a204b"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie_id {movie_id}: {e}")
        return "https://via.placeholder.com/100x150.png?text=No+Image"
# Movie Tab
with tabs[0]:
    st.header("🎬 Movie Recommendation")
    selected_movie_name = st.selectbox("Select a movie", movies_list)

    if st.button("Recommend Movies"):
        st.subheader("Top 5 Movie Recommendations")
        recommended_movies = recommend_movie(selected_movie_name)
        col1, col2, col3 = st.columns(3)

        for i,j in enumerate(recommended_movies):
            with [col1, col2, col3][i % 3]:
                st.image(movie_poster(j[0]), width=100)
                st.markdown(f"**{j[1]}**")

# Book Tab
with tabs[1]:
    st.header("📚 Book Recommendation")
    selected_book_name = st.selectbox("Select a book", books_list)

    if st.button("Recommend Books"):
        st.subheader("Top 5 Book Recommendations")
        recommended_books = recommend_book(selected_book_name)

        col1, col2, col3= st.columns(3)

        for idx, (title, thumb) in enumerate(recommended_books):
            with [col1, col2, col3][idx % 3]:
                st.image(thumb, width=100)
                st.markdown(f"**{title}**")