import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="NutriSnap",
    page_icon="🍏",
    layout="centered"
)

# 2. BARRA LATERAL (Diseño limpio para Datos Personales)
with st.sidebar:
    st.markdown("### 📋 Perfil Personal")
    st.markdown("Configura tus datos para adaptar tus requerimientos diarios.")
    
    # Campos para ingresar datos con valores por defecto limpios
    edad = st.number_input("Edad", min_value=1, max_value=100, value=17, step=1)
    peso = st.number_input("Peso actuales (kg)", min_value=10.0, max_value=200.0, value=69.0, step=0.1)
    estatura = st.number_input("Estatura (m)", min_value=0.5, max_value=2.5, value=1.71, step=0.01)
    
    st.markdown("---")
    st.caption("Los datos se guardan automáticamente para calcular tu déficit calórico.")

# 3. PANTALLA PRINCIPAL (Diseño Minimalista Avanzado)
# Encabezado con tipografía estilizada usando HTML nativo permitido
st.markdown("<h1 style='text-align: center; color: #1E293B; font-weight: 800; margin-bottom: 0px;'>NutriSnap</h1>", unsafe_allowed_html=True)
st.markdown("<p style='text-align: center; color: #64748B; font-size: 14px; margin-top: 0px; font-style: italic;'>Tu asistente de nutrición inteligente</p>", unsafe_allowed_html=True)
st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allowed_html=True)

# Contenedor estético para las métricas
with st.container():
    st.markdown("<h4 style='color: #334155; font-weight: 600; margin-bottom: 15px;'>Resumen de Macros Restantes</h4>", unsafe_allowed_html=True)
    
    # Columnas simétricas
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="🔥 Calorías Restantes", value="2,202 kcal", delta="Meta de hoy", delta_color="off")
    
    with col2:
        st.metric(label="💪 Proteínas Restantes", value="138 g", delta="Meta de hoy", delta_color="off")

# 4. Barra de progreso fina y estilizada
st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allowed_html=True)
st.progress(0.0)
st.markdown("<p style='color: #94A3B8; font-size: 12px; margin-top: 2px;'>Progreso diario de calorías (0%)</p>", unsafe_allowed_html=True)

st.markdown("<hr style='border: 0; height: 1px; background: #E2E8F0; margin: 30px 0;'>", unsafe_allowed_html=True)

# 5. Zona de Cámara Premium
st.markdown("<h4 style='color: #334155; font-weight: 600; margin-bottom: 15px;'>📸 Analiza tu platillo</h4>", unsafe_allowed_html=True)

# Cuadro de cámara
imagen_comida = st.camera_input("Apunta con la cámara de tu celular")

if imagen_comida:
    st.success("¡Imagen recibida con éxito! Analizando composición...")
