import pickle
import streamlit as st
import requests

st.image(r"C:\Users\DEEPAK\Downloads\avengers endgame roated.jpeg")

def fetch_poster(movi_id):
    url = f"https://api.themoviedb.org/3/movie/{movi_id}?api_key=0d591d0d5d299c8857b57e7da9c9c9a6"
    movie_image = requests.get(url)
    movie_image = movie_image.json()
    movie_image_path = str(movie_image['poster_path'])
    #movie_image_path = movie_image['belongs_to_collection']['poster_path']
    full_movie_image_path = "https://image.tmdb.org/t/p/w500"+movie_image_path
    return full_movie_image_path

def recommned(movie_name):
    index = movie[movie['original_title'] == movie_name].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda x : x[1])
    for i in distance[1:11]:
        movie_id = movie.iloc[i[0]].movie_id
        recommende_movie_poster.append(fetch_poster(movie_id))
        recommende_movie_name.append(movie.iloc[i[0]].original_title)
    return recommende_movie_name, recommende_movie_poster


st.header("Movie Recommendation System")
movie = pickle.load(open(r'C:\Users\DEEPAK\INTERNSHIP ASSINGMENT\Assingment -12\Assingment -12 Data\movie_data.pkl', 'rb'))
similarity = pickle.load(open(r'C:\Users\DEEPAK\INTERNSHIP ASSINGMENT\Assingment -12\Assingment -12 Data\similarity_data.pkl', 'rb'))

movie_list = movie['original_title'].values
selected_movie = st.selectbox('Enter Movie Name', movie_list)

recommende_movie_name = []
recommende_movie_poster = []

if st.button('Show Recommendation'):
    recommned(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommende_movie_name[0])
        st.image(recommende_movie_poster[0])
    with col2:
        st.text(recommende_movie_name[1])
        st.image(recommende_movie_poster[1])
    with col3:
        st.text(recommende_movie_name[2])
        st.image(recommende_movie_poster[2])
    with col4:
        st.text(recommende_movie_name[3])
        st.image(recommende_movie_poster[3])
    with col5:
        st.text(recommende_movie_name[4])
        st.image(recommende_movie_poster[4])
    