# Table of contents
* [General Information](#general-information)
* [Problem Solving](#problem-solving)
* [Run Project](#run-project)

# General Information

In this project, I built a recommendation system based on Content-based. Besides, I divided into two types which the first one will recommend without ratings data and the second one will based on ratings data

In the first model, I have used [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). It contains two dataset that are credits and movies, credits will contain data about cast, crew and title while the movies contain the information of movies such as genre, budget, overview or homepage. This model base only on features of a movie and find top N similar movies

In the recommender based on ratings, I have used [MovieLens](https://grouplens.org/datasets/movielens/) dataset which is stable and contain 100,000 ratings from 1000 users on 1700 movies. Released 4/1998. I built a recommendation system based on Content-Based method with ratings data. It will recommend movies for a user based on their ratings data of other movies

# Problem Solving

### Collaborative Filtering

This model just only uses the TF-IDF and Cosine Similarity. 
* Firstly, I apply TF-IDF technique for measuring the importance probability of each word in `tags` (tags is a overall information of a movie)
* Then, I consider each row of TF-IDF matrix like a vector about features of a movie, called features vector
* I apply Cosine Similarity to figure out the angle between target movie and each of recommended movies, the lower angle is, the recommended movies are more similar to target one

![image](https://github.com/Narius2030/Recommendation-System/assets/94912102/8e791c80-7f1e-4e74-a5ce-f96a15df720c)

* The work flow

![image](https://github.com/Narius2030/Recommendation-System/assets/103951468/2c00c073-760b-4c4e-91be-5edf13febd97)

# Run Project

> Note: 
> * Python version 3.8+
> * Install all packages in *requirements.txt*

#### Run Streamlit webpage
```python
streamlit run app.py
```

#### Demo Image

* Recommendation tab

![image](https://github.com/Narius2030/Recommendation-System/assets/103951468/7539cec3-616e-4599-b89f-507ce0fbddfd)

![image](https://github.com/Narius2030/Recommendation-System/assets/103951468/124192b6-b064-4748-a4fa-dca2216fd5e6)



