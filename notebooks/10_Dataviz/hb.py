import plotly.express as px
df = px.data.gapminder()

import streamlit as st

continentes = df['continent'].unique()
continente = st.selectbox(label='Seleccione continente', options=continentes)

mask = df['pais']==continente
dff = df[mask]

fig = px.line(data_frame=dff, x='year', y='lifeExp')
st.plotly_chart(fig)

