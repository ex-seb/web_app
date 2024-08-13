import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("metro.csv")

st.header('web app')
hist_button = st.button('Construir un histograma')
