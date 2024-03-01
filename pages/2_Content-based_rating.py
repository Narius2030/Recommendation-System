import streamlit as st
import numpy as np
import pandas as pd
import sys
sys.path.append('model')
from ContentBasedWithRating import recommend

st.set_page_config(layout="wide")
st.header("Content-based Recommender System With Ratings")
dataframe_tab, recd_tab = st.tabs(['Data table','Recommender'])

#define dataframes
i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure', 
            'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 
            'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('./data/ml-100k/u.item', sep='|', names=i_cols, encoding='latin-1')
p_cols = ['movie_id', 'poster']
item_posters = pd.read_csv('./data/ml-100k/movie_poster.csv', sep=',', names=p_cols)

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
        recommends = pd.DataFrame({'movie_id':movie_ids, 'scores':scores, 
                                   'title':items['movie title'].to_list()})
        recommends = recommends.merge(item_posters, how='left', on='movie_id')
        recommends = recommends.sort_values(by=['scores'], ascending=False).reset_index()
        # st.write(recommends)
        
        col1, col2, col3, col4, col5 = st.columns(5)
        col6, col7, col8, col9, col10 = st.columns(5)
        with col1:
            st.text(recommends.loc[0, 'title'])
            st.image(recommends.loc[0, 'poster'])
        with col2:
            st.text(recommends.loc[1, 'title'])
            st.image(recommends.loc[1, 'poster'])
        with col3:
            st.text(recommends.loc[2, 'title'])
            st.image(recommends.loc[2, 'poster'])
        with col4:
            st.text(recommends.loc[3, 'title'])
            st.image(recommends.loc[3, 'poster'])
        with col5:
            st.text(recommends.loc[4, 'title'])
            st.image(recommends.loc[4, 'poster'])
        with col6:
            st.text(recommends.loc[5, 'title'])
            st.image(recommends.loc[5, 'poster'])
        with col7:
            st.text(recommends.loc[6, 'title'])
            st.image(recommends.loc[6, 'poster'])
        with col8:
            st.text(recommends.loc[7, 'title'])
            st.image(recommends.loc[7, 'poster'])
        with col9:
            st.text(recommends.loc[8, 'title'])
            st.image(recommends.loc[8, 'poster'])
        with col10:
            st.text(recommends.loc[9, 'title'])
            st.image(recommends.loc[9, 'poster'])