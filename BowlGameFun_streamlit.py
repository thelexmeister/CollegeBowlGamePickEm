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

st.header('Fun Facts for Hawaii Bowl')
st.image('https://cdn.vox-cdn.com/thumbor/3C6VGijImlfq9l6tMJb3zwOTE1s=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/21875845/1190467819.jpg.jpg', width=300)
st.text('Photo by Photo by Darryl Oumi/Getty Images')
st.subheader('Officially started in 2002 (as that name)')
st.subheader('I grew up watching this bowl game and always felt it was odd - not football weather!\
             Started in 1936 as the Poi Bowl. Then through the 40s to early 50s (when it was played - it was stopped because of WW1 and WW2) it was\
             the PINEAPPLE BOWL!!! YUM! From 1982 - 2000 (this is my time growing up with the bowl game)\
             it was called the Aloha Bowl. But did you know this game was moved to Seattle, called the\
             Seattle Bowl, from 2000-2002.\
             Hawaii has the most appearances (9). This will be the third appearance for the two teams playing this year. ')

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
    
