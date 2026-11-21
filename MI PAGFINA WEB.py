import streamlit as st
import time

st.set_page_config(page_title="Portafolio Robótica", page_icon="🤖", layout="centered")

# Pon aquí el link final de tu app (.streamlit.app) cuando lo tengas
LINK_APP = "https://tuproyecto.streamlit.app"

st.markdown("""
<style>
.stApp { background-color: #0e1117; color: white; }
h1 { color: #00ffcc; text-align: center; text-shadow: 0 0 12px #00ffcc; }
.tarjeta {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #b300ff;
    margin-bottom: 20px;
}
.qr-box {
    border: 2px dashed #00ffcc;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    margin: 15px auto;
    max-width: 230px;
    background-color: #161920;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 Portafolio de Robótica")

# Menú lateral interactivo (ideal para celular)
with st.sidebar:
    st.header("📱 Escanea para abrir")
    st.markdown(f"""
    <div class="qr-box">
        <img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={LINK_APP}" alt="QR">
        <p style="color:#00ffcc; font-size:12px; margin-top:8px;">Abre este proyecto en tu celular</p>
    </div>
    """, unsafe_allow_html=True)
    st.info("Usa las pestañas de la pantalla principal para probar los simuladores interactivos.")

# Pestañas interactivas para que el profe navegue fácil
tab1, tab2, tab3, tab4 = st.tabs([
    "🦾 Brazo Robótico", 
    "🚗 Conexión PC y Carros", 
    "⚔️ Robots y 3D", 
    "⭐ Calificar"
])

# --- PESTAÑA 1: BRAZO ROBÓTICO + LEDS INTERACTIVOS ---
with tab1:
    st.markdown('<div class="tarjeta"><h3>🦾 Mano / Brazo Robótico y Luces LED</h3><p>Armamos un brazo robótico articulado con servomotores MG90S y control de iluminación LED.</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.image("brazo.jpg", caption="Prototipo con servomotores MG90S", use_container_width=True)
    with col2:
        st.subheader("🎛️ Panel de Control")
        pinza = st.slider("Abrir / Cerrar Pinza (°)", 0, 180, 90)
        base = st.slider("Rotación de Base (°)", 0, 180, 45)
        led = st.toggle("💡 Encender Luces LED", value=True)
        
        if led:
            st.success(f"LEDs ENCENDIDOS | Pinza: {pinza}° | Base: {base}°")
        else:
            st.warning(f"LEDs APAGADOS | Pinza: {pinza}° | Base: {base}°")

# --- PESTAÑA 2: CONEXIÓN DE COMPUTADORAS Y CARROS ---
with tab2:
    st.markdown('<div class="tarjeta"><h3>🚗 Conexión de Computadoras</h3><p>Hicimos pasar una pelotita y carros de carreras de la pantalla de una computadora a otra en red.</p></div>', unsafe_allow_html=True)
    
    st.image("carro.png", caption="Vehículo transferido entre pantallas", width=350)
    
    st.subheader("🏁 Simulador de Transferencia")
    velocidad = st.select_slider("Selecciona la velocidad de envío:", options=["Lento", "Normal", "Turbo 🚀"])
    
    if st.button("Enviar carro a la otra pantalla ➡️"):
        barra = st.progress(0, text="Transmitiendo datos entre PC 1 y PC 2...")
        for porcentaje in range(100):
            time.sleep(0.01 if velocidad == "Turbo 🚀" else 0.02)
            barra.progress(porcentaje + 1, text=f"Transfiriendo carro... {porcentaje + 1}%")
        st.balloons()
        st.success("¡El carro cruzó a la segunda computadora con éxito!")

# --- PESTAÑA 3: RESTO DE PROYECTOS INTERACTIVOS ---
with tab3:
    st.markdown('<div class="tarjeta"><h3>⚔️ Pelea de Robots</h3><p>Controlamos robots a distancia mediante señales de internet para competir en la arena.</p></div>', unsafe_allow_html=True)
    if st.button("⚡ Activar ataque del robot"):
        st.toast("¡Señal enviada por Wi-Fi! Impacto registrado.", icon="🤖")
        st.info("Estado: Robot conectado y respondiendo en tiempo real.")

    st.markdown('<div class="tarjeta"><h3>🧊 Impresión 3D en Tinkercad</h3><p>Diseñamos piezas mecánicas personalizadas en Tinkercad listas para fabricar en 3D.</p></div>', unsafe_allow_html=True)
    with st.expander("Ver detalles técnicos del diseño 3D"):
        st.write("- **Software:** Autodesk Tinkercad")
        st.write("- **Material:** Filamento PLA")
        st.write("- **Piezas diseñadas:** Soportes para servomotores y articulaciones.")

# --- PESTAÑA 4: EVALUACIÓN DEL PROFESOR ---
with tab4:
    st.
