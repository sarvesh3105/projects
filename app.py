
import streamlit as st
import pickle
import requests
import pandas as pd

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8dd4ffd7e25bfaba04d97520d13604dc'.format(movie_id))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distance=similarity[movie_index]
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters


movies_dict=pickle.load(open('movies_dict1.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity2.pkl','rb'))
st.header('Movie Recommendation')


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values
)

if st.button('Show Recommendation'):
    names,poster=recommend(selected_movie)

    col1, col2, col3,col4,col5= st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
