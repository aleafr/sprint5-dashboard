import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Análise de anúncios de carros")

# ler dados
car_data = pd.read_csv("vehicles_us.csv")

st.write("Pré-visualização dos dados:")
st.dataframe(car_data.head())

# limpar dados para gráficos
car_data = car_data.dropna(subset=["price", "model_year", "odometer"])

# histograma
if st.checkbox("Mostrar histograma do odómetro"):
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# gráfico de dispersão
if st.checkbox("Mostrar gráfico de dispersão (preço vs ano do modelo)"):
    fig_scatter = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)
