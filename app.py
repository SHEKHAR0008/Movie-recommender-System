import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

# import requests
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
#
#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer da4979a119db5aaf28b05f4aee2a204b"
#     }
#
#     response = requests.get(url, headers=headers)
#     return "https://image.tmdb.org/t/p/w500/" + response.json()


def recommend(movie):
    movie_idx = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_idx]
    idx = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    ret_lst = []
    for i in idx:
        # print(fetch_poster(i[0]))
        ret_lst.append(movies.iloc[i[0]].title)

    return ret_lst



selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies_list,
)

st.write("You selected:", selected_movie_name)
if st.button("Recommend"):
    lst = recommend(selected_movie_name)
    for i in lst:
        st.write(i)


