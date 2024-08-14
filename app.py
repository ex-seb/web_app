import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("metro.csv")
linea_a = df[df['linea'].str.contains('Linea A')]

st.header('Uso de la línea A del Sistema de Transporte Colectivo Metro en Ciudad de México durante Junio de 2024')

hist_checkbox = st.checkbox('Trazar un histograma')

if hist_checkbox:

    st.write(
        'Creación de un histograma para el conjunto de datos del metro en Ciudad de México')

    fig = px.histogram(linea_a, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox = st.checkbox('Trazar un gráfico de dispersión')

if scatter_checkbox:
    st.write(
        'Creación de un gráfico de dispersión para el conjunto de datos del metro en Ciudad de México')
    fig = px.scatter(linea_a, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox = st.checkbox('Trazar un gráfico de barras')

if bar_checkbox:
    st.write(
        'Creación de un gráfico de barras para el conjunto de datos del metro en Ciudad de México')
    fig = px.bar(linea_a, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)
