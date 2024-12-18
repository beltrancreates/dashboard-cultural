# Importar librerías necesarias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium

# Configurar el título del dashboard
st.title("Dashboard de Análisis Cultural y Experiencias")
st.markdown("### Visualiza datos culturales, asistencia a eventos y presupuesto")

# Cargar datos ficticios
data = pd.DataFrame({
    'Evento': ['Concierto', 'Teatro', 'Exposición', 'Festival'],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia'],
    'Asistencia': [500, 300, 200, 400],
    'Presupuesto': [10000, 8000, 6000, 9000]
})

# Mostrar los datos en una tabla interactiva
st.subheader("📊 Datos de los eventos culturales")
st.dataframe(data)

# Gráfico de barras: Asistencia por tipo de evento
st.subheader("🎟️ Asistencia por Tipo de Evento")
fig, ax = plt.subplots()
ax.bar(data['Evento'], data['Asistencia'], color=['blue', 'orange', 'green', 'purple'])
ax.set_title('Asistencia por Tipo de Evento')
ax.set_xlabel('Evento')
ax.set_ylabel('Asistencia')
st.pyplot(fig)

# Gráfico de dispersión: Presupuesto vs Asistencia
st.subheader("💰 Relación entre Presupuesto y Asistencia")
fig, ax = plt.subplots()
ax.scatter(data['Presupuesto'], data['Asistencia'], color='red', s=100)
ax.set_title('Presupuesto vs Asistencia')
ax.set_xlabel('Presupuesto (€)')
ax.set_ylabel('Asistencia')
st.pyplot(fig)

# Mapa interactivo con ubicaciones de los eventos
st.subheader("🗺️ Mapa de Ubicación de Eventos")
m = folium.Map(location=[40.416775, -3.703790], zoom_start=6)

# Coordenadas ficticias de las ubicaciones
ubicaciones = [
    [40.416775, -3.703790],  # Madrid
    [41.385063, 2.173404],   # Barcelona
    [37.389092, -5.984459],  # Sevilla
    [39.469907, -0.376288]   # Valencia
]

# Añadir marcadores al mapa
for i, row in data.iterrows():
    folium.Marker(
        location=ubicaciones[i],
        popup=f"{row['Evento']} - {row['Ciudad']}\nAsistencia: {row['Asistencia']}",
        tooltip="Clic para más info"
    ).add_to(m)

# Mostrar el mapa interactivo en Streamlit
st_folium(m, width=700, height=500)

# Mensaje final
st.markdown("**¡Explora estos datos para optimizar tus proyectos culturales!** 🚀")
