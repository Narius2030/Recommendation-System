import requests
import streamlit as st
import numpy as np
import pandas as pd
import sys
sys.path.append('model')
from ContentBasedWithRating import ContentBasedWithRating, recommend

st.set_page_config(layout="wide")
st.header("Content-based Recommender System With Ratings")
dataframe_tab, recd_tab = st.tabs(['Data table','Recommender'])

#define dataframes
i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure', 
            'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 
            'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('./data/ml-100k/u.item', sep='|', names=i_cols, encoding='latin-1')

u_cols =  ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('./data/ml-100k/u.user', sep='|', names=u_cols, encoding='latin-1')

Yhat = np.loadtxt('./artificats/recommends.csv', delimiter=',')

with dataframe_tab:
    st.write('Movie table', items)
    st.write('User table',users)
    
with recd_tab:
    user_id = st.sidebar.selectbox(
        'Choose a user id',
        users.iloc[:,0]
    )
    age = users.at[user_id-1, 'age']
    sex = users.at[user_id-1, 'sex']
    occupation = users.at[user_id-1, 'occupation']
    
    st.sidebar.text_input(label='Age',value='{}'.format(age))
    st.sidebar.text_input(label='Sex',value='{}'.format(sex))
    st.sidebar.text_input(label='Occupation',value='{}'.format(occupation))
    
    if st.sidebar.button('Recommend'):
        movie_ids, scores = recommend(items, user_id, Yhat)
        recommend = pd.DataFrame({'movie_id':movie_ids, 'scores':scores, 'title':items['movie title'].to_list()})
        recommend = recommend.sort_values(by=['scores'], ascending=False)
        st.table(recommend.head(10))