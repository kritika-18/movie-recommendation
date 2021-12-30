import streamlit as st
import pickle
import pandas as pd
import requests

def details(movie_id):
    url="https://api.themoviedb.org/3/movie/"+str(movie_id[0])+"?api_key=540d8bd185fa200dd0d8a918f054dcec&language=en-US"
    data=requests.get(url)
    data=data.json()

    poster = 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

    overview=data['overview']

    release=data['release_date']

    rating = data['vote_average']
    dur=data['runtime']
    return poster,overview, release, rating, dur

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/"+str(movie_id)+"?api_key=540d8bd185fa200dd0d8a918f054dcec&language=en-US"
    data=requests.get(url)
    data=data.json()

    poster = 'https://image.tmdb.org/t/p/w500/' + data['poster_path']
    return poster

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)

        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

similarity=pickle.load(open('similarity.pkl','rb'))

st.image('Title-Picture.jpg')
st.header('Apni Movies!')
movies_dict=pickle.load(open('movie_dict.pkl','rb'))

movies=pd.DataFrame(movies_dict)

selected_movie_name = st.selectbox(
'What do you like to watch?',
movies['title'].values)



if st.button('Recommend'):

    movie_index = movies[movies['title'] == selected_movie_name].index[0]
    current_movie_id = movies[movies['title'] == selected_movie_name].movie_id
    poster, overview, release, rating, dur = details(current_movie_id.values)
    c1,c2=st.columns([1,1.5])
    with c1:
        st.image(poster,width=200)
    with c2:

        st.write('Overview: '+str(overview))

        st.write('Release date: '+str(release))

        st.write('Rating: ' + str(rating) + '⭐')
        st.write('Duration: '+str(dur)+' minutes')

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



st.write('by Kritika Chauhan')

