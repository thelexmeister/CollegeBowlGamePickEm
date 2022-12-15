# A short code to make a simple dashboard to distribute information

import streamlit as st
import pandas as pd

dfr = pd.read_csv('BowlGamePracticeRecords.csv')
dfB = pd.read_csv('BowlGames.csv')
dfG = pd.read_csv('Entries_2022.csv')

st.set_page_config(page_title='Bowl Game Pick-em', layout="wide")

# Add a sidebar to the web page. 
st.markdown('---')
# Sidebar Configuration
st.sidebar.image('https://www.shutterstock.com/image-photo/july-26-2018-pasadena-california-260nw-1144270187.jpg', width=200)
st.sidebar.markdown('Bowl Game Fun Challenge')
st.sidebar.markdown('We only made picks for 10 games, just to make it easier, but there are 40+ bowl games this year so enjoy!')
st.sidebar.markdown('')
st.sidebar.markdown('Remember, we are in this for the fun, but how YOU define fun is up to you!')
st.sidebar.markdown('')

st.sidebar.markdown('---')
st.sidebar.write('Developed by X')

# Display the Data in the App.
st.image('https://media.istockphoto.com/id/1343884923/photo/low-angle-view-of-a-college-style-football-at-a-yard-line-with-dramatic-lighting.jpg?b=1&s=170667a&w=0&k=20&c=dEFqtXMW-PMzCkOxWGggiNH8IItYP0GybpAPyHJcazI=')
st.header('WELCOME TO THE COLLEGE BOWL PICK-EM 2022-23')
st.header('Scroll down to see your picks, fun facts about upcoming bowl games and where you stand.')

st.header('Fun Facts for The Vegas Bowl')
st.image('https://kslsports.com/wp-content/uploads/2020/12/Las-Vegas-Bowl-620x370.jpg', width=300)
st.text('Photo by Ethan Miller/Getty Images')
st.subheader('Officially started in 1992')
st.subheader('This was originally the California Raisin Bowl, but it needed a new home. And\
             because of how slow Vegas is around Christmas, Vegas pushed for the game to be moved there.')

st.header('Bowl Games and Results')
st.dataframe(dfB)

col1,col2 = st.columns(2)
with col1:
    st.header('Who Picked Whom?')
    st.subheader('Scroll to the right to see everyone.')
    st.dataframe(dfG)
with col2:
    st.header('How well is everyone doing?')
    st.subheader('Is anyone at 100%?')
    st.dataframe(dfr)
    
