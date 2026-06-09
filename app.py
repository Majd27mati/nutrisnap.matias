import streamlit as st

# 1. Configuración de la página (Estilo limpio)
st.set_page_config(
    page_title="NutriSnap",
    page_icon="🍏",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo CSS personalizado para fuentes y bordes minimalistas
st.markdown("""
    <style>
    .big-title { font-size: 32px; font-weight: 700; color: #2E3A59; letter-spacing: -0.5px; margin-bottom: 5px; }
    .subtitle { font-size: 16px; color: #8F9BB3; margin-bottom: 30px; }
    .section-title { font-size: 18px; font-weight: 600; color: #2E3A59; margin-bottom: 15px; }
    div[data-testid="stMetricValue"] { font-size: 28px !important; font-weight: 600 !important; }
    </style>
""", unsafe_allowed_html=True)

# 2. Encabezado Minimalista
st.markdown('<div class="big-title">NutriSnap</div>', unsafe_allowed_html=True)
st.markdown('<div class="subtitle">Asistente de nutrición inteligente y registro diario</div>', unsafe_allowed_html=True)

st.markdown("---")

# 3. Panel de Métricas Detalladas (En columnas limpias)
st.markdown('<div class="section-title">Resumen de Macros Restantes</div>', unsafe_allowed_html=True)

col1, col2 = st.columns(2)

with col1:
    # st.metric crea un diseño de tarjeta impecable por defecto
    st.metric(label="🔥 Energía", value="2,202 kcal", delta="Consumidas: 0 kcal", delta_color="inverse")

with col2:
    st.metric(label="💪 Proteína", value="138 g", delta="Consumidas: 0 g", delta_color="inverse")

# 4. Progreso Visual Fino
st.markdown(" ")
st.caption("Progreso diario de calorías")
st.progress(0.0) # Barra de progreso minimalista (va de 0.0 a 1.0)

st.markdown("---")

# 5. Zona de Captura Impecable
st.markdown('<div class="section-title">📸 Análisis de Platillo</div>', unsafe_allowed_html=True)

# Contenedor limpio para la cámara
with st.container():
    imagen_comida = st.camera_input("Apunta a tu plato para calcular macros")

    if imagen_comida:
        with st.spinner("Analizando composición nutricional..."):
            # Aquí irá tu lógica de análisis más adelante
            st.success("¡Imagen recibida con éxito!")
