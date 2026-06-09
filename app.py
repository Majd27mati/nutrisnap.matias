import streamlit as st
import datetime

# Configuración de la página
st.set_page_config(page_title="NutriSnap - Contador de Macros", page_icon="🍏", layout="centered")

st.title("🍏 NutriSnap")
st.subheader("Tu asistente de nutrición inteligente")
st.markdown("---")

# --- ESTADO INICIAL (Base de datos temporal en memoria) ---
if "calorias_consumidas" not in st.session_state:
    st.session_state.calorias_consumidas = 0
if "proteinas_consumidas" not in st.session_state:
    st.session_state.proteinas_consumidas = 0
if "historial" not in st.session_state:
    st.session_state.historial = []

# --- PANEL LATERAL: CONFIGURACIÓN DEL PERFIL ---
st.sidebar.header("👤 Tu Perfil y Metas")
peso = st.sidebar.number_input("Peso (kg):", min_value=30, max_value=200, value=69)
estatura = st.sidebar.number_input("Estatura (cm):", min_value=100, max_value=250, value=171)
edad = st.sidebar.number_input("Edad:", min_value=10, max_value=100, value=17)
objetivo = st.sidebar.selectbox("Tu Objetivo:", ["Déficit Calórico (Perder Grasa)", "Volumen (Ganar Músculo)"])

# Lógica matemática para calcular metas diarias (Fórmula Mifflin-St Jeor)
geb = (10 * peso) + (6.25 * estatura) - (5 * edad) + 5
gasto_mantenimiento = geb * 1.55 # Factor para actividad moderada (gimnasio 3-5 días)

if "Déficit" in objetivo:
    meta_calorias = int(gasto_mantenimiento - 400)
else:
    meta_calorias = int(gasto_mantenimiento + 400)

meta_proteinas = int(peso * 2) # Estándar de 2g de proteína por kg

# Mostrar metas calculadas en la barra lateral
st.sidebar.markdown("### 🎯 Tus Metas Diarias:")
st.sidebar.write(f"**Calorías Objetivo:** {meta_calorias} kcal")
st.sidebar.write(f"**Proteínas Objetivo:** {meta_proteinas} g")

if st.sidebar.button("🔄 Reiniciar Contador Diario"):
    st.session_state.calorias_consumidas = 0
    st.session_state.proteinas_consumidas = 0
    st.session_state.historial = []
    st.rerun()

# --- PANEL PRINCIPAL: DASHBOARD DIARIO ---
col1, col2 = st.columns(2)

calorias_restantes = meta_calorias - st.session_state.calorias_consumidas
proteinas_restantes = meta_proteinas - st.session_state.proteinas_consumidas

with col1:
    st.metric(label="🔥 Calorías Restantes", value=f"{calorias_restantes} kcal", delta=f"Consumidas: {st.session_state.calorias_consumidas}")
with col2:
    st.metric(label="💪 Proteínas Restantes", value=f"{proteinas_restantes} g", delta=f"Consumidas: {st.session_state.proteinas_consumidas}g")

# Barras de progreso visuales
st.markdown("*Progreso de Calorías:*")
porcentaje = min(float(st.session_state.calorias_consumidas) / float(meta_calorias), 1.0)
st.progress(porcentaje)
