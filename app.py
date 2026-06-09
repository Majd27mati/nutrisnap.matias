import streamlit as st

# 1. Configuración de la página (Limpia y minimalista)
st.set_page_config(
    page_title="NutriSnap",
    page_icon="🍏",
    layout="centered"
)

# 2. Encabezado Minimalista (Formatos limpios usando markdown directo)
st.markdown("# *NutriSnap*")
st.markdown("### Tu asistente de nutrición inteligente")
st.markdown("---")

# 3. Panel de Métricas Detalladas en Columnas
st.markdown("#### *Resumen de Macros Restantes*")

col1, col2 = st.columns(2)

with col1:
    # Usamos st.metric nativo (es ultra minimalista y no necesita CSS)
    st.metric(label="🔥 Calorías Restantes", value="2,202 kcal", delta="Consumidas: 0")

with col2:
    st.metric(label="💪 Proteínas Restantes", value="138 g", delta="Consumidas: 0g")

# 4. Barra de progreso delgada
st.markdown(" ")
st.progress(0.0)
st.caption("Progreso diario de calorías")

st.markdown("---")

# 5. Zona de Captura con la Cámara
st.markdown("#### *📸 Analiza tu platillo*")
imagen_comida = st.camera_input("Toma una foto de tu comida para calcular los macros")

if imagen_comida:
    st.success("¡Imagen recibida con éxito! Analizando...")
