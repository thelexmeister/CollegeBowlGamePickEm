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
st.image('https://media.wired.com/photos/5a3af51805f16a0c504434ee/master/pass/football-FA.jpg', width = 300)
st.header('WELCOME TO THE COLLEGE BOWL PICK-EM 2022-23')
st.header('Scroll down to see your picks, fun facts about upcoming bowl games and where you stand.')

st.header('DEC 31st - Sugar and Fiesta Bowl')
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRczlRcqmq__rpgu-zU_M8nawTv5jakUcKh2Q&usqp=CAU', width=300)
st.text('HA HA HA - wrong Sugar Bowl...on purpose. I grew up skiing here..l')
st.subheader(' ')
st.subheader("Sugar Bowl: Started in 1935. So many of these games started in 1935?!?!?.\
             I'm just going to share the picture...this is from the 40s. So cool! ")
st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Tulane_Stadium_Sugar_Bowl_This_Week_in_New_Orleans_Dec_4_1948.jpg/405px-Tulane_Stadium_Sugar_Bowl_This_Week_in_New_Orleans_Dec_4_1948.jpg',width=300)
st.subheader(' ')
st.subheader('Fiesta Bowl: This only started in 1971. But here we go, a BCS semi-final!\
             THE Ohio State has made the most appearances (9). Arizona State has the most appearances\
             for a Pac-12 school. There were a lot of fun things I learned, but this got me:\
             Jan 2, 2021 Brock Purdy was the Offensive MVP!')
st.subheader(' ')
st.subheader(' ')

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
    
