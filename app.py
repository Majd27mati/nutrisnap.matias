import streamlit as st

# 1. Configuración de la interfaz
st.set_page_config(
    page_title="NutriSnap",
    page_icon="🍏",
    layout="centered"
)

# 2. BARRA LATERAL (Tus datos personales ordenados a un lado)
with st.sidebar:
    st.markdown("## 📋 Perfil Personal")
    st.caption("Ajusta tus datos para personalizar tus metas.")
    
    # Inputs nativos con tus datos guardados por defecto
    edad = st.number_input("Edad", min_value=1, max_value=100, value=17, step=1)
    peso = st.number_input("Peso Actual (kg)", min_value=10.0, max_value=200.0, value=69.0, step=0.1)
    estatura = st.number_input("Estatura (m)", min_value=0.5, max_value=2.5, value=1.71, step=0.01)
    
    st.divider()
    st.caption("Déficit calórico activo.")

# 3. PANTALLA PRINCIPAL (Limpia y Estética)
st.title("NutriSnap")
st.caption("Tu asistente de nutrición inteligente")

st.divider()

# Contenedor para agrupar las métricas como una tarjeta premium
with st.container(border=True):
    st.markdown("### *Resumen de Macros Restantes*")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="🔥 Energía", value="2,202 kcal", delta="Meta diaria")
    with col2:
        st.metric(label="💪 Proteína", value="138 g", delta="Meta diaria")
    
    # Barra de progreso y texto fino dentro de la tarjeta
    st.progress(0.0)
    st.caption("Progreso diario de calorías (0%)")

st.divider()

# 4. ZONA DE CÁMARA
st.markdown("### *📸 Analiza tu platillo*")

with st.container(border=True):
    imagen_comida = st.camera_input("Apunta con la cámara de tu celular")

    if imagen_comida:
        st.success("¡Imagen recibida con éxito! Iniciando análisis...")
