import requests
import streamlit as st
import pickle
import pandas as pd
import sys
sys.path.append(r'D:\HCMUTE\Namba\HK02\DataMining\Middle_Term\Recommendation-System\model')
from CollaborativeFiltering import CF

st.set_page_config(layout="wide")
st.header("Collaborative_Filtering Recommender System With Ratings")
movies = pickle.load(open("./artificats/movies.pkl", "rb"))
similarities = pickle.load(open("./artificats/similarities.pkl", "rb"))
movie_titles = movies['title'].values

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']

ratings_base = pd.read_csv('D:/HCMUTE/Namba/HK02/DataMining/Middle_Term/Recommendation-System/data/ml-100k/ua.base', sep='\t', names=r_cols, encoding='latin-1')
ratings_test = pd.read_csv('D:/HCMUTE/Namba/HK02/DataMining/Middle_Term/Recommendation-System/data/ml-100k/ub.test', sep='\t', names=r_cols, encoding='latin-1')

rate_train = ratings_base.values
rate_test = ratings_test.values

# indices start from 0
rate_train[:, :2] -= 1
rate_test[:, :2] -= 1

rs = CF(rate_train, k=30, uuCF=1)
rs.fit()

selected_user = st.text_input("Enter your user", value="")
selected_user = int(selected_user) if selected_user.strip().isdigit() else None


def fetch_poster(movie_id) -> str:
    url = "https://api.themoviedb.org/3/movie/{}?api_key=3fed181afbe284769c6a495334dc66ea&language=en-US".format(movie_id)
    resp = requests.get(url)
    poster_path = resp.json().get('poster_path')
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(title) -> tuple:
    recommendations = rs.recommend_top_k(selected_user, top_k = 10)
    recommendation_ids = [pair[0] for pair in recommendations]
    recommended_movie_names = []
    recommended_movie_posters = []
    for distance in recommendation_ids:
        print(distance)
        movie_id = movies.loc[distance, 'movie_id']
        recommended_movie_names.append(movies.loc[distance, 'title'])
        recommended_movie_posters.append(fetch_poster(movie_id))
        
    return recommended_movie_names, recommended_movie_posters

if st.button("Show recommendations"):
    name, poster = recommend(selected_user)

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


def predicted(title) -> tuple:
    user_Predicted = rs.get_user_ratings(selected_user)
    # recommendation_ids = [pair[0] for pair in user_Predicted]
    recommended_movie_names = []
    recommended_movie_posters = []
    for distance in user_Predicted:
        print(distance)
        movie_id = movies.loc[distance, 'movie_id']
        recommended_movie_names.append(movies.loc[distance, 'title'])
        recommended_movie_posters.append(fetch_poster(movie_id))
        
    return recommended_movie_names, recommended_movie_posters

if st.button("User predicted"):
    names, posters = predicted(selected_user)
    
    num_movies = len(names)
    num_rows = num_movies // 5 + (1 if num_movies % 5 != 0 else 0)

    for row in range(num_rows):
        cols = st.columns(5)
        start_idx = row * 5
        end_idx = min((row + 1) * 5, num_movies)
        
        for idx, col in enumerate(cols):
            if start_idx + idx < end_idx:
                col.text(names[start_idx + idx])
                col.image(posters[start_idx + idx])