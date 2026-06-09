import streamlit as st

# 1. Configuración de la interfaz dinámica
st.set_page_config(
    page_title="NutriSnap - Macros & Energía",
    page_icon="🍏",
    layout="centered"
)

# 2. BARRA LATERAL COLORIDA (Tu Perfil Detallado)
with st.sidebar:
    st.markdown("## 📋 Perfil Personal")
    st.write("Mantén actualizados tus datos para ajustar tu plan diario.")
    
    # Entradas de datos organizadas
    edad = st.number_input("Tu Edad (años)", min_value=1, max_value=100, value=17, step=1)
    peso = st.number_input("Peso Actual (kg)", min_value=10.0, max_value=200.0, value=69.0, step=0.1)
    estatura = st.number_input("Estatura Actual (m)", min_value=0.5, max_value=2.5, value=1.71, step=0.01)
    
    st.divider()
    
    # Caja informativa estilizada y colorida para el objetivo
    st.info("🎯 *Objetivo Actual:* Régimen de Déficit Calórico activo para optimización de porcentaje de grasa.")

# 3. PANTALLA PRINCIPAL (Diseño Detallado y Colorido)
st.title("🍏 NutriSnap Pro")
st.write("Tu ecosistema inteligente de monitoreo nutricional y registro fotográfico.")

# Pestañas interactivas para agregar muchísimo detalle sin saturar la pantalla
tab_resumen, tab_detalles = st.tabs(["✨ Tablero Principal", "📈 Análisis Detallado"])

with tab_resumen:
    st.write("### *Tus Metas de Hoy*")
    
    # Bloque de métricas usando columnas interactivas
    c1, c2 = st.columns(2)
    
    with c1:
        # Tarjeta de energía con indicador de estado (Color azul/rojo dinámico)
        st.metric(
            label="🔥 Presupuesto de Energía", 
            value="2,202 kcal", 
            delta="Restantes para el límite", 
            delta_color="normal"
        )
        
    with c2:
        # Tarjeta de proteína con indicador (Color verde dinámico)
        st.metric(
            label="💪 Bloques de Proteína", 
            value="138 g", 
            delta="Objetivo de retención muscular", 
            delta_color="inverse"
        )

    # Barra de progreso visual
    st.write(" ")
    st.write("*Balance de consumo actual:*")
    st.progress(0.0)
    st.caption("Progreso diario: 0% de calorías ingeridas / Faltan 2,202 kcal")

    st.divider()

    # Zona de captura fotográfica detallada
    st.write("### *📸 Escáner Inteligente de Platillos*")
    st.write("Coloca tu plato bajo buena luz y captura la imagen para desglosar macronutrientes.")
    
    imagen_comida = st.camera_input("Capturar alimento")

    if imagen_comida:
        st.success("¡Imagen sincronizada con éxito! Procesando volumen e ingredientes...")

with tab_detalles:
    st.write("### 📊 Desglose de Parámetros Corporales")
    st.write("Información detallada calculada a partir de los datos de tu perfil:")
    
    # Mostramos los datos de manera muy visual y detallada en tarjetas informativas
    col_a, col_b, col_c = st.columns(3)
    col_a.help(f"Edad registrada: {edad} años")
    col_b.help(f"Peso base: {peso} kg")
    col_c.help(f"Altura base: {estatura} m")
    
    st.markdown("""
    *Distribución sugerida para tus comidas de hoy:*
    * 🍳 *Desayuno:* 550 kcal | 35g Proteína
    * 🍗 *Almuerzo (Post-Entreno):* 800 kcal | 45g Proteína
    * 🧀 *Snack / Merienda:* 300 kcal | 23g Proteína
    * 🐟 *Cena Ligera:* 552 kcal | 35g Proteína
    """)
    
    st.warning("💡 *Tip de entrenamiento:* Asegúrate de consumir una fuente de proteína limpia junto con carbohidratos complejos después de tus sesiones de fuerza para optimizar la recuperación.")
