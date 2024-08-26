import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("metro.csv")

linea_a = df[df['linea'] == ('Linea A')]
linea_1 = df[df['linea'] == ('Linea 1')]
linea_2 = df[df['linea'] == ('Linea 2')]
linea_3 = df[df['linea'] == ('Linea 3')]
linea_4 = df[df['linea'] == ('Linea 4')]
linea_5 = df[df['linea'] == ('Linea 5')]
linea_6 = df[df['linea'] == ('Linea 6')]
linea_7 = df[df['linea'] == ('Linea 7')]
linea_8 = df[df['linea'] == ('Linea 8')]
linea_9 = df[df['linea'] == ('Linea 9')]
linea_b = df[df['linea'] == ('Linea B')]
linea_12 = df[df['linea'] == ('Linea 12')]


st.header('Afluencia en STC Metro.')
st.header('Ciudad de México, Junio 2024.')

st.subheader('Línea 1', divider="rainbow")

hist_checkbox_1 = st.checkbox(
    'Trazar un histograma para el conjunto de datos sobre la línea 1')

if hist_checkbox_1:

    st.write(
        'Creación de un histograma')

    fig = px.histogram(linea_1, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox_1 = st.checkbox(
    'Trazar un gráfico de dispersión para el conjunto de datos sobre la línea 1')

if scatter_checkbox_1:
    st.write(
        'Creación de un gráfico de dispersión')
    fig = px.scatter(linea_1, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox_1 = st.checkbox(
    'Trazar un gráfico de barras para el conjunto de datos sobre la línea 1')

if bar_checkbox_1:
    st.write(
        'Creación de un gráfico de barras')
    fig = px.bar(linea_1, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Línea 2', divider="blue")

hist_checkbox_2 = st.checkbox(
    'Trazar un histograma para el conjunto de datos sobre la línea 2')

if hist_checkbox_2:

    st.write(
        'Creación de un histograma')

    fig = px.histogram(linea_2, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox_2 = st.checkbox(
    'Trazar un gráfico de dispersión para el conjunto de datos sobre la línea 2')

if scatter_checkbox_2:
    st.write(
        'Creación de un gráfico de dispersión')
    fig = px.scatter(linea_2, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox_2 = st.checkbox(
    'Trazar un gráfico de barras para el conjunto de datos sobre la línea 2')

if bar_checkbox_2:
    st.write(
        'Creación de un gráfico de barras')
    fig = px.bar(linea_2, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Línea 3', divider="green")

hist_checkbox_3 = st.checkbox(
    'Trazar un histograma para el conjunto de datos sobre la línea 3')

if hist_checkbox_3:

    st.write(
        'Creación de un histograma')

    fig = px.histogram(linea_3, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox_3 = st.checkbox(
    'Trazar un gráfico de dispersión para el conjunto de datos sobre la línea 3')

if scatter_checkbox_3:
    st.write(
        'Creación de un gráfico de dispersión')
    fig = px.scatter(linea_3, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox_3 = st.checkbox(
    'Trazar un gráfico de barras para el conjunto de datos sobre la línea 3')

if bar_checkbox_3:
    st.write(
        'Creación de un gráfico de barras')
    fig = px.bar(linea_3, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Línea 4', divider="rainbow")

hist_checkbox_4 = st.checkbox(
    'Trazar un histograma para el conjunto de datos sobre la línea 4')

if hist_checkbox_4:

    st.write(
        'Creación de un histograma')

    fig = px.histogram(linea_4, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox_4 = st.checkbox(
    'Trazar un gráfico de dispersión para el conjunto de datos sobre la línea 4')

if scatter_checkbox_4:
    st.write(
        'Creación de un gráfico de dispersión')
    fig = px.scatter(linea_4, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox_4 = st.checkbox(
    'Trazar un gráfico de barras para el conjunto de datos sobre la línea 4')

if bar_checkbox_4:
    st.write(
        'Creación de un gráfico de barras')
    fig = px.bar(linea_4, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Línea 5', divider="rainbow")

hist_checkbox_5 = st.checkbox(
    'Trazar un histograma para el conjunto de datos sobre la línea 5')

if hist_checkbox_5:

    st.write(
        'Creación de un histograma')

    fig = px.histogram(linea_5, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox_5 = st.checkbox(
    'Trazar un gráfico de dispersión para el conjunto de datos sobre la línea 5')

if scatter_checkbox_5:
    st.write(
        'Creación de un gráfico de dispersión')
    fig = px.scatter(linea_5, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox_5 = st.checkbox(
    'Trazar un gráfico de barras para el conjunto de datos sobre la línea 5')

if bar_checkbox_5:
    st.write(
        'Creación de un gráfico de barras')
    fig = px.bar(linea_5, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Línea 6', divider="red")

hist_checkbox_6 = st.checkbox(
    'Trazar un histograma para el conjunto de datos sobre la línea 6')

if hist_checkbox_6:

    st.write(
        'Creación de un histograma')

    fig = px.histogram(linea_6, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox_6 = st.checkbox(
    'Trazar un gráfico de dispersión para el conjunto de datos sobre la línea 6')

if scatter_checkbox_6:
    st.write(
        'Creación de un gráfico de dispersión')
    fig = px.scatter(linea_6, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox_6 = st.checkbox(
    'Trazar un gráfico de barras para el conjunto de datos sobre la línea 6')

if bar_checkbox_6:
    st.write(
        'Creación de un gráfico de barras')
    fig = px.bar(linea_6, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Línea 7', divider="orange")

hist_checkbox_7 = st.checkbox(
    'Trazar un histograma para el conjunto de datos sobre la línea 7')

if hist_checkbox_7:

    st.write(
        'Creación de un histograma')

    fig = px.histogram(linea_7, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox_7 = st.checkbox(
    'Trazar un gráfico de dispersión para el conjunto de datos sobre la línea 7')

if scatter_checkbox_7:
    st.write(
        'Creación de un gráfico de dispersión')
    fig = px.scatter(linea_7, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox_7 = st.checkbox(
    'Trazar un gráfico de barras para el conjunto de datos sobre la línea 7')

if bar_checkbox_7:
    st.write(
        'Creación de un gráfico de barras')
    fig = px.bar(linea_7, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Línea 8', divider="green")

hist_checkbox_8 = st.checkbox(
    'Trazar un histograma para el conjunto de datos sobre la línea 8')

if hist_checkbox_8:

    st.write(
        'Creación de un histograma')

    fig = px.histogram(linea_8, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox_8 = st.checkbox(
    'Trazar un gráfico de dispersión para el conjunto de datos sobre la línea 8')

if scatter_checkbox_8:
    st.write(
        'Creación de un gráfico de dispersión')
    fig = px.scatter(linea_8, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox_8 = st.checkbox(
    'Trazar un gráfico de barras para el conjunto de datos sobre la línea 8')

if bar_checkbox_8:
    st.write(
        'Creación de un gráfico de barras')
    fig = px.bar(linea_8, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Línea 9', divider="rainbow")

hist_checkbox_9 = st.checkbox(
    'Trazar un histograma para el conjunto de datos sobre la línea 9')

if hist_checkbox_9:

    st.write(
        'Creación de un histograma')

    fig = px.histogram(linea_9, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox_9 = st.checkbox(
    'Trazar un gráfico de dispersión para el conjunto de datos sobre la línea 9')

if scatter_checkbox_9:
    st.write(
        'Creación de un gráfico de dispersión')
    fig = px.scatter(linea_9, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox_9 = st.checkbox(
    'Trazar un gráfico de barras para el conjunto de datos sobre la línea 9')

if bar_checkbox_9:
    st.write(
        'Creación de un gráfico de barras')
    fig = px.bar(linea_9, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Línea A', divider="violet")

hist_checkbox_a = st.checkbox(
    'Trazar un histograma para el conjunto de datos sobre la línea A')

if hist_checkbox_a:

    st.write(
        'Creación de un histograma')

    fig = px.histogram(linea_a, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox_a = st.checkbox(
    'Trazar un gráfico de dispersión para el conjunto de datos sobre la línea A')

if scatter_checkbox_a:
    st.write(
        'Creación de un gráfico de dispersión')
    fig = px.scatter(linea_a, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox_a = st.checkbox(
    'Trazar un gráfico de barras para el conjunto de datos sobre la línea A')

if bar_checkbox_a:
    st.write(
        'Creación de un gráfico de barras')
    fig = px.bar(linea_a, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Línea B', divider="grey")

hist_checkbox_b = st.checkbox(
    'Trazar un histograma para el conjunto de datos sobre la línea B')

if hist_checkbox_b:

    st.write(
        'Creación de un histograma')

    fig = px.histogram(linea_b, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox_b = st.checkbox(
    'Trazar un gráfico de dispersión para el conjunto de datos sobre la línea B')

if scatter_checkbox_b:
    st.write(
        'Creación de un gráfico de dispersión')
    fig = px.scatter(linea_b, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox_b = st.checkbox(
    'Trazar un gráfico de barras para el conjunto de datos sobre la línea B')

if bar_checkbox_b:
    st.write(
        'Creación de un gráfico de barras')
    fig = px.bar(linea_b, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Línea 12', divider="rainbow")

hist_checkbox_12 = st.checkbox(
    'Trazar un histograma para el conjunto de datos sobre la línea 12')

if hist_checkbox_12:

    st.write(
        'Creación de un histograma')

    fig = px.histogram(linea_12, x="estacion", y='afluencia',
                       labels={
                           "estacion": "Estación",
                           "afluencia": "Afluencia"
                       }, title="Afluencia por estación")

    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox_12 = st.checkbox(
    'Trazar un gráfico de dispersión para el conjunto de datos sobre la línea 12')

if scatter_checkbox_12:
    st.write(
        'Creación de un gráfico de dispersión')
    fig = px.scatter(linea_12, x="estacion", y="afluencia", color="tipo_pago",
                     labels={"estacion": "Estación",
                             "afluencia": "Afluencia",
                             "tipo_pago": "Tipo de Pago"},
                     title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)

bar_checkbox_12 = st.checkbox(
    'Trazar un gráfico de barras para el conjunto de datos sobre la línea 12')

if bar_checkbox_12:
    st.write(
        'Creación de un gráfico de barras')
    fig = px.bar(linea_12, x="estacion", y="afluencia", color="tipo_pago",
                 labels={"estacion": "Estación",
                         "afluencia": "Afluencia",
                         "tipo_pago": "Tipo de Pago"},
                 title="Tipo de pago por estación")
    st.plotly_chart(fig, use_container_width=True)
