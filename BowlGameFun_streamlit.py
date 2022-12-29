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

st.header('Orange Bowl and Sun Bowl')
st.image('https://ca-times.brightspotcdn.com/dims4/default/8653424/2147483647/strip/true/crop/5871x3914+265+0/resize/2400x1600!/quality/80/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F25%2Fe1%2Fbc41f46a4caea1f0bd676ee23eb5%2Fsd-photos-1staff-892853-sd-me-holiday-bowl-101.JPG', width=300)
st.text('Photo from The San Diego Union-Tribune')
st.subheader('Orange Bowl is completely ORANGE (Tennessee and Clemson) - wow, take things literally why not?!?!?')
st.subheader('Sun Bowl is played in "the pass"! Good ol El Paso! What a great place! Not a joke, not sarcastic - I was born there!')
st.subheader(' ')
st.subheader('Orange Bowl: Started in 1935. Only a few times has a non-ranked team played in the bowl game.\
             Only in 1935, 1936, 1938, and 1944, were both teams not ranked. The first year there was an MVP (1965) it was Joe Namath. ')
st.subheader(' ')
st.subheader('SUN BOWL!!!!! So we know it is in a great city (El Paso), which is a mile high - take that Denver!\
             Started in 1935! Two old games today! Oh this is fun: the 1940 game was between the Arizona State Teachers College\
             at Tempe and the Catholic University Cardinals - the game ended 0-0! Fun Pac12 fact - this is a Pac10/12 tie-in and \
             only Colorado and Cal have not appeared in the Sun Bowl. Pac12 is 19-12-1.')
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
    
