#Make sure this is done first

#pip install streamlit -q
#pip install tornado==5.1
# change directory first: cd \Users\lexig\Desktop\BowlGameFun
# TO RUN: streamlit run C:\Users\lexig\Desktop\BowlGameFun\BowlGameFun_streamlit.py


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#df = pd.read_csv('C:/Users/lexig/Desktop/BowlGameFun/BowlGamePractice.csv')
dfr = pd.read_csv('C:/Users/lexig/Desktop/BowlGameFun/BowlGamePracticeRecords.csv')
dfB = pd.read_csv('C:/Users/lexig/Desktop/BowlGameFun/BowlGames.csv')
dfG = pd.read_csv('C:/Users/lexig/Desktop/BowlGameFun/Entries_2022.csv')

st.set_page_config(page_title='Bowl Game Pick-em', layout="wide")


# Add a sidebar to the web page. 
st.markdown('---')
# Sidebar Configuration
st.sidebar.image('https://www.shutterstock.com/image-photo/july-26-2018-pasadena-california-260nw-1144270187.jpg', width=300)
st.sidebar.markdown('WOU - HEXS Bowl Game Fun Challenge')
st.sidebar.markdown('We only made picks for 10 games, but each bowl game has a reason.')
st.sidebar.markdown('Vegas Bowl: This is a Pac12 bowl, and a favorite of Utah.')
st.sidebar.markdown('Potato Bowl: Have you seen the mascot for the bowl?')
st.sidebar.markdown('Independence Bowl: Ok, ok, it is the wrong Independence, but the pseudo-local connection was too much to pass up.')
st.sidebar.markdown("Hawai'i Bowl: I grew up watching this bowl in CA thinking why is everyone so excited about being in Hawaii?")
st.sidebar.markdown('Holiday Bowl: This bowl has a rich history, for the west coast, and it is a Pac10/12 tie-in, so some of our favorites might be playing here or have a history here.')
st.sidebar.markdown('Orange Bowl: This, along with the Sun and Sugar Bowls, is the second longest running bowl game, it started in 1935. And a call back to the idea of the bowl games being just local games, celebrating local highlights.')
st.sidebar.markdown('Sun Bowl: Yes it is old, but it is now sponsored by Tony the Tiger and it is in my birth city!')
st.sidebar.markdown("Sugar Bowl: Yes, just like the Orange and Sun, it has tradition, but this is also the site of Utah's greatest ever bowl win. Hey, I made the game!")
st.sidebar.markdown('Cotton Bowl: History, tradition, and I remember growing up watching this game on New Years.')
st.sidebar.markdown("Rose Bowl: Have I mentioned I'm from California? It is a Pac8/10/12 Bowl and it is the longest running bowl game EVERY. Started in 1902!")

st.sidebar.markdown('')

st.sidebar.markdown('---')
st.sidebar.write('Developed by Lex Gidley')

# Display the Data in the App.
st.image('https://media.istockphoto.com/id/1343884923/photo/low-angle-view-of-a-college-style-football-at-a-yard-line-with-dramatic-lighting.jpg?b=1&s=170667a&w=0&k=20&c=dEFqtXMW-PMzCkOxWGggiNH8IItYP0GybpAPyHJcazI=')
st.header('WELCOME TO THE WOU - HEXS COLLEGE BOWL PICK-EM 2022-23')
st.header('Scroll down to see your picks, fun facts about upcoming bowl games and where you stand.')

st.header('Fun Facts for The Vegas Bowl')
st.image('https://kslsports.com/wp-content/uploads/2020/12/Las-Vegas-Bowl-620x370.jpg')
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
    

