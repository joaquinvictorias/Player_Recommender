import pandas as pd
import numpy as np
import streamlit as st
from sklearn.metrics.pairwise import cosine_distances

df = pd.read_csv('pca.csv')

def show_predict_page():
    st.title('Player Recommender')
    st.subheader('Based on the 2023/24 season data for the Big 5 European Leagues')

    # Player's name
    name = sorted(list(df['Player']))
    names = st.sidebar.selectbox('Name', name)

    # Player's position
    position = sorted(list(df['Pos'].unique()))
    position.insert(0, 'All')

    # Create a multiselect widget with some options
    positions = st.sidebar.multiselect('Position', position)

    # If 'All' is selected, select all other options
    if 'All' in positions:
        positions = position[1:]
    
    # Player's competition
    competition = sorted(list(df['Comp'].unique()))
    competition.insert(0, 'All')

    # Create a multiselect widget with some options
    competitions = st.sidebar.multiselect('Competition', competition)

    # If 'All' is selected, select all other options
    if 'All' in competitions:
        competitions = competition[1:]

    # Player's age

    # Define the age range
    min_age = df['Age'].min()
    max_age = df['Age'].max()

    # Add a slider widget to select the age range
    min_ages, max_ages =  st.sidebar.slider('Age', min_value=min_age, max_value=max_age, value=(min_age, max_age))

    # Number of results
    results = st.sidebar.slider('Number of results', 1, 10, 5)

    # Fetch the player vector
    def getStats(name):
        return df.query('Player == @name').iloc[:,11:]

    # Fetch cosine similarity between two player vectors
    def similarity(player1, player2):
        return 1 - cosine_distances(getStats(player1), getStats(player2))

    calculate = st.sidebar.button('Calculate')
    if calculate:

        similarity_vectorize = np.vectorize(similarity)
        pivot = pd.DataFrame(similarity_vectorize(names, df['Player'])) \
            .sort_values(by=0, ascending=False) \
                .iloc[1:].rename(columns={0: 'Similarity'})
        pivot = pivot.join(df.iloc[:,:11])
        pivot = pivot[['Player', 'Nation', 'Pos', 'Squad', 'Comp', 'Age', 'Similarity']] \
            .rename(columns={'Pos': 'Position', 'Comp': 'Competition'})
        pivot['Similarity'] = pivot['Similarity'] * 100
        pivot['Similarity'] = pivot['Similarity'].map('{:.2f}'.format).astype(str) + '%'
        pivot = pivot.query('Position == @positions')
        pivot = pivot.query('Competition == @competitions')
        pivot = pivot.query('Age >= @min_ages & Age <= @max_ages')
        pivot = pivot.reset_index(drop=True)
        st.table(pivot.head(results))

show_predict_page()