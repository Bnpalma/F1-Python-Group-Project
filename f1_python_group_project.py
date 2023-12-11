import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Streamlit app starts here
st.set_page_config(page_title="Brawn GP: A F1 Story", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
selected_section = st.sidebar.radio("Go to", ("Home", "Overview of F1 Teams", "2003-2008 Season Analysis", "2009 Winning Probability Analysis", "2008 Season Aftermath", "First Race of 2009", "Brawn GP Car Analysis", "2009 First 7 Races Analysis", "Rest of the 2009 Season", "Season Finale"))

# Home Page
if selected_section == "Home":
    st.title("Brawn GP: A F1 Story")
    st.write("Welcome to an interactive exploration of Brawn GP's remarkable journey in Formula 1. Navigate through the sections to discover their legacy.")

# Overview of F1 Teams
elif selected_section == "Overview of F1 Teams":
    st.header("Overview of Every Team in F1")
