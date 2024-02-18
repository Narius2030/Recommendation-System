import requests
import streamlit as st
import pickle

st.header("Film Recommendation System")
movies = pickle.load(open("./artificats/movies.pkl", "rb"))
similarities = pickle.load(open("./artificats/similarities.pkl", "rb"))
movie_titles = movies['title'].values

selected_movie = st.selectbox (
    "Choose your movie",
    movie_titles
)

def fetch_poster(movie_id) -> str:
    url = " https://api.themoviedb.org/3/movie/{}?api_key=3fed181afbe284769c6a495334dc66ea&language=en-US".format(movie_id)
    resp = requests.get(url)
    poster_path = resp.json().get('poster_path')
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(title) -> tuple:
    index = movies[movies['title'] == title].index[0]
    distances = sorted(list(enumerate(similarities[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for distance in distances[1:11]:
        movie_id = movies.loc[distance[0], 'movie_id']
        recommended_movie_names.append(movies.loc[distance[0], 'title'])
        recommended_movie_posters.append(fetch_poster(movie_id))
        
    return recommended_movie_names, recommended_movie_posters

if st.button("Show recommendations"):
    name, poster = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    col6, col7, col8, col9, col10 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])
    with col6:
        st.text(name[5])
        st.image(poster[5])
    with col7:
        st.text(name[6])
        st.image(poster[6])
    with col8:
        st.text(name[7])
        st.image(poster[7])
    with col9:
        st.text(name[8])
        st.image(poster[8])
    with col10:
        st.text(name[9])
        st.image(poster[9])