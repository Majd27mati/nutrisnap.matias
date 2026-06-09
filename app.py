[11:50 a.m., 9/6/2026] .: import streamlit as st

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
[11:54 a.m., 9/6/2026] .: import streamlit as st

# 1. Configuración de la interfaz
st.set_page_config(
    page_title="NutriSnap",
    page_icon="🍏",
    layout="centered"
)

# 2. DISEÑO VISUAL ULTRA-DETALLADO Y COLORIDO (CSS Seguro)
st.markdown("""
    <style>
    /* Fondo general con un degradado sutil y colorido (pasteles modernos) */
    .stApp {
        background: linear-gradient(135deg, #F0F4FF 0%, #FFF5F5 50%, #E8F5E9 100%);
    }
    
    /* Estilo para el título principal */
    .main-title {
        font-family: 'Poppins', sans-serif;
        font-size: 42px;
        font-weight: 800;
        background: linear-gradient(45deg, #1E3A8A, #10B981);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
    }
    
    /* Subtítulos sutiles */
    .main-subtitle {
        text-align: center;
        color: #64748B;
        font-size: 15px;
        font-weight: 500;
        margin-bottom: 30px;
    }
    
    /* Tarjetas contenedoras detalladas y con sombras sutiles */
    .custom-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(148, 163, 184, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.7);
        margin-bottom: 25px;
    }
    
    /* Encabezados dentro de las tarjetas */
    .card-header {
        font-size: 18px;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Bloques de métricas personalizados y coloridos */
    .metric-box {
        background: #FFFFFF;
        padding: 15px;
        border-radius: 15px;
        border-left: 5px solid #3B82F6; /* Azul para calorías */
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
    }
    .metric-box.protein {
        border-left: 5px solid #10B981; /* Verde para proteína */
    }
    
    .metric-label { font-size: 13px; color: #64748B; font-weight: 600; text-transform: uppercase; }
    .metric-value { font-size: 26px; color: #1E293B; font-weight: 800; margin: 2px 0; }
    .metric-delta { font-size: 12px; color: #3B82F6; font-weight: 500; }
    .metric-delta.protein { color: #10B981; }
    </style>
""", unsafe_allowed_html=True)

# 3. PANEL LATERAL (Configuración del Perfil)
with st.sidebar:
    st.markdown("### 📋 Configuración de Perfil")
    st.caption("Ajusta tus datos para recalcular tus requerimientos diarios.")
    
    edad = st.number_input("Edad (años)", min_value=1, max_value=100, value=17, step=1)
    peso = st.number_input("Peso Actual (kg)", min_value=10.0, max_value=200.0, value=69.0, step=0.1)
    estatura = st.number_input("Estatura (m)", min_value=0.5, max_value=2.5, value=1.71, step=0.01)
    
    st.divider()
    st.info("💡 Modo: Déficit Calórico Activo")

# 4. PANTALLA PRINCIPAL
st.markdown('<div class="main-title">NutriSnap</div>', unsafe_allowed_html=True)
st.markdown('<div class="main-subtitle">Tu asistente de nutrición inteligente y registro de macros</div>', unsafe_allowed_html=True)

# --- TARJETA 1: RESUMEN NUTRICIONAL DETALLADO ---
st.markdown("""
<div class="custom-card">
    <div class="card-header">📊 Resumen de Macros Restantes</div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px;">
        <div class="metric-box">
            <div class="metric-label">🔥 Energía</div>
            <div class="metric-value">2,202 kcal</div>
            <div class="metric-delta">Meta diaria restante</div>
        </div>
        <div class="metric-box protein">
            <div class="metric-label">💪 Proteína</div>
            <div class="metric-value">138 g</div>
            <div class="metric-delta protein">Meta diaria restante</div>
        </div>
    </div>
</div>
""", unsafe_allowed_html=True)

# Barra de progreso estilizada
st.caption("Progreso del consumo calórico diario")
st.progress(0.0)

# --- TARJETA 2: ESCÁNER DE CÁMARA PREMIUM ---
st.markdown('<div class="custom-card">', unsafe_allowed_html=True)
st.markdown('<div class="card-header">📸 Escáner de Platillos</div>', unsafe_allowed_html=True)
st.markdown('<p style="font-size: 13px; color: #64748B; margin-top:-10px; margin-bottom:15px;">Captura una foto de tu comida para desglosar sus ingredientes y macronutrientes automáticamente.</p>', unsafe_allowed_html=True)

imagen_comida = st.camera_input("Apunta con la cámara de tu celular")

if imagen_comida:
    st.markdown('<div style="background-color: #E8F5E9; color: #2E7D32; padding: 12px; border-radius: 10px; font-size: 14px; font-weight: 500; margin-top: 15px;">✔️ ¡Imagen capturada con éxito! Analizando composición nutricional...</div>', unsafe_allowed_html=True)

st.markdown('</div>', unsafe_allowed_html=True)
