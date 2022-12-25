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

st.header('We have made it! To another local interest bowl game: The Holiday Bowl!')
st.image('https://ca-times.brightspotcdn.com/dims4/default/8653424/2147483647/strip/true/crop/5871x3914+265+0/resize/2400x1600!/quality/80/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F25%2Fe1%2Fbc41f46a4caea1f0bd676ee23eb5%2Fsd-photos-1staff-892853-sd-me-holiday-bowl-101.JPG', width=300)
st.text('Photo from The San Diego Union-Tribune')
st.subheader('AHHHH! Good ol San Diego!')
st.subheader(' ')
st.subheader('Ok, boy does the bowl have some West Coast history! So, first it started in 1978 to give the WAC and automatic bowl bid after\
              the Fiesta Bowl pulled its association with the WAC when Arizona and Arizona State bolted for the Pac8 - to make the Pac10.')
st.subheader(' ')
st.subheader('While there have been many games of note for the Pac10/12, because ironically it then became a tie-in for the Pac10/12 since 1998,\
              the most controversial game was 1984...UGH. I will let you read the write up on wikipedia for the full story, but, in short, the game\
              was relatively close the whole game. Ended 24-17. WOW sounds great, right? This was the year an undefeated BYU team BARELY beat a\
              6-5 Michigan team to "secure" the National Championship. No matter how bad we feel the National Champion is decided now, it is\
              decidedly better than it was. (e_e)!')
st.subheader(' ')
st.subheader('BYU is the school that has visited the most, but Oregon has gone 4 times and has a winning record. Let us hope they keep it up!')
              
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
    
