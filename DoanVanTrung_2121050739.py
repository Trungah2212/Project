import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Configure the layout to full width
st.set_page_config(layout="wide")

# Sidebar
st.sidebar.markdown("Select a range on the slider (it represents movie score) to view the total number of movies in a genre that falls within that range")
st.sidebar.slider('Choose a value:', 1.00, 10.00, (3.00, 4.00))
st.sidebar.markdown("Select your preferred genre(s) and year to view the movies released that year and on that genre")
st.sidebar.multiselect('Choose Genre:', ['Animation', 'Horror', 'Fantasy','Romance'])
st.sidebar.selectbox("Chọn năm:", list(range(1980, 2020)))

# Header and Columns
st.header("Interactive Dashboard")
st.subheader("Interact with this dashboard using the widgets on the sidebar")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Lists of movies filtered by year and Genre Type to search")
    data = {
        "name": ["Altered States", "Bon Voyage, Charlie Brown(and Don't Come Back!!)", "Friday the 13th", "Prom Night", "The Awakening", "The Boogey Man", "The Fog", "The King and the Mockingbird", "Xanadu"],
        "genre": ["Horror", "Animation", "Horror", "Horror", "Horror", "Horror", "Horror", "Animation", "Fantasy"],
        "year": [1980, 1980, 1980, 1980, 1980, 1980, 1980, 1980, 1980],
    }

    st.table(data)

with col2:    
    st.subheader("User score of movies and their genre")
    genre = ["Action","Adventure", "Animation", "Biography", "Comedy", "Crime", "Drama", "Horror"]
    score = [34, 12, 2.5, 1,38,4, 7.5, 17.5]

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(genre, score, color='b')

    # Format the plot
    ax.set_xlabel('genre')
    ax.set_ylabel('score')
    ax.set_ylim(0, 40) 
    ax.grid(True)
    ax.set_facecolor('lightgrey') 

    # Display the plot
    st.pyplot(fig)