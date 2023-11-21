import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np

st.title('Polo Tecnológico en Córdoba')

# Cargar el DataFrame desde el archivo CSV
DF_accesos_localidad = pd.read_csv(
    '15-AccesosaInternetfijoportecnologiaylocalidad_2791751699377796593.csv')


# Supongamos que 'Tipo de tecnología' es la columna que contiene los tipos de conexión
total_coverage = DF_accesos_localidad['Cantidad de conexiones'].groupby(
    DF_accesos_localidad['Tipo de tecnología']).sum()

# Crear una app de Streamlit
st.title('Cobertura total de conexiones por tipo de tecnología')

# Mostrar el gráfico en Streamlit
fig, ax = plt.subplots(figsize=(10, 6))
total_coverage.sort_values().plot(kind='barh', color='skyblue', ax=ax)
plt.title('Cobertura total de conexiones por tipo de tecnología')
plt.xlabel('Cantidad de conexiones')
plt.ylabel('Tipo de tecnología')
st.pyplot(fig)
