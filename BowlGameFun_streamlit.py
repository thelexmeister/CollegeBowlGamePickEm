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

st.header('JAN 2nd - The Gran-daddy of them all!')
st.image('https://rosebowlinstitute.org/cdn/rose-bowl-stadium-home-hero-2.jpg', width=300)
st.text('https://rosebowlinstitute.org/')
st.subheader(' ')

st.subheader("Rose bowl: 1902 - first time it was played. Then picked up again in 1916 and hasn't stopped since.\
            In 2021, it was played in TX not in CA. The only other time this was done was\
            1942 just after Pearl Harbor. They moved it because Duke didn't want to go to the West Coast so they\
            invited Oregon State go to them to play."
st.subheader(' ')
st.subheader('USC has played the most times (34) - HA HA! Not there this year!! USC and Michigan have met 8 times!\
            There is just so much history with this game...gotta love it!')
st.subheader('GO UTES!')
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
    
