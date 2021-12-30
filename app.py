import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=540d8bd185fa200dd0d8a918f054dcec&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

st.header('Movie Recommender System')
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

movies=pd.DataFrame(movies_dict)

selected_movie_name = st.selectbox(
'What do you like to watch?',
movies['title'].values)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3, col4, col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

    with col1:
        st.text(names[0])
        st.image(posters[0])



