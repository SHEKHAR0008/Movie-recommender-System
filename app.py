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

def recommend_book(book,top_n=5):
    try:
        books_idx = books[books['title'] == book].index[0]
    except IndexError:
        return ["Book not found in dataset."]
    top_similar= similarity_books[books_idx][:top_n]
    recommend = books.iloc[[k for k in top_similar]]
    return list(zip(recommend['title'], recommend['thumbnail']))


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
        return "https://img.freepik.com/free-vector/man-saying-no-concept-illustration_114360-14222.jpg"

def display_fixed_image(img_url, width=200, height=300):
    st.markdown(
        f"""
        <img src="{img_url}" 
             style="width:{width}px; height:{height}px; object-fit:cover; border-radius:8px; border:1px solid #ccc;"
             alt="Image"/>
        """,
        unsafe_allow_html=True
    )

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
                display_fixed_image(movie_poster(j[0]))
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
                display_fixed_image(thumb)
                st.markdown(f"**{title}**")