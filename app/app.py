import streamlit as st
import joblib
import re
import os

# ─── Configuracion de la pagina ───────────────────────
st.set_page_config(
    page_title="Detector de Idiomas",
    page_icon="🌍",
    layout="centered"
)
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ─── Estilos ──────────────────────────────────────────
st.markdown("""
    <style>
        .resultado {
            font-size: 2em;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        .confianza {
            text-align: center;
            font-size: 1.1em;
            color: gray;
            margin-top: 5px;
        }
        .bandera {
            font-size: 3em;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# ─── Cargar el modelo ─────────────────────────────────
@st.cache_resource
def cargar_modelo():
    base = os.path.join(os.path.dirname(__file__), '..', 'modelo')
    modelo = joblib.load(os.path.join(base, 'modelo_idiomas.pkl'))
    vectorizador = joblib.load(os.path.join(base, 'vectorizador.pkl'))
    return modelo, vectorizador

# ─── Normalizar texto ─────────────────────────────────
def normalizar(texto):
    texto = texto.lower()
    texto = re.sub(r'\d+', ' ', texto)
    texto = re.sub(r'[^a-záéíóúñüçàèùâêîôûãõäöß\s]', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto)
    return texto.strip()

# ─── Datos de idiomas ─────────────────────────────────
INFO_IDIOMAS = {
    'Spanish':    {'nombre': 'Español',    'bandera': '🇪🇸', 'color': '#FF6B6B'},
    'English':    {'nombre': 'Inglés',     'bandera': '🇬🇧', 'color': '#4ECDC4'},
    'French':     {'nombre': 'Francés',    'bandera': '🇫🇷', 'color': '#45B7D1'},
    'Portugeese': {'nombre': 'Portugués',  'bandera': '🇧🇷', 'color': '#96CEB4'},
}

# ─── Interfaz ─────────────────────────────────────────
st.title("🌍 Detector de Idiomas")
st.markdown("Escribe o pega cualquier texto y el sistema detectará automáticamente en qué idioma está escrito.")
st.markdown("---")

# Verificar si el modelo existe
ruta_modelo = os.path.join(os.path.dirname(__file__), '..', 'modelo', 'modelo_idiomas.pkl')
if not os.path.exists(ruta_modelo):
    st.error("⚠️ El modelo no está entrenado todavía. Por favor cierra esta ventana y vuelve a ejecutar INICIAR.bat (Windows) o iniciar.sh (Linux).")
    st.stop()

# Cargar modelo
try:
    modelo, vectorizador = cargar_modelo()
except Exception as e:
    st.error(f"Error cargando el modelo: {e}")
    st.stop()

# Área de texto
texto_usuario = st.text_area(
    "✍️ Escribe tu texto aquí:",
    height=200,
    placeholder="Ejemplo: El procesamiento del lenguaje natural es fascinante..."
)

# Botón de detección
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    detectar = st.button("🔍 Detectar Idioma", use_container_width=True)

# ─── Resultado ────────────────────────────────────────
if detectar:
    if not texto_usuario.strip():
        st.warning("⚠️ Por favor escribe algún texto antes de detectar.")
    elif len(texto_usuario.strip()) < 10:
        st.warning("⚠️ El texto es muy corto. Escribe al menos una oración completa.")
    else:
        with st.spinner("Analizando el texto..."):
            texto_limpio = normalizar(texto_usuario)
            texto_vec = vectorizador.transform([texto_limpio])

            idioma_detectado = modelo.predict(texto_vec)[0]
            probabilidades = modelo.predict_proba(texto_vec)[0]
            clases = modelo.classes_
            confianza = max(probabilidades) * 100

            info = INFO_IDIOMAS.get(idioma_detectado, {
                'nombre': idioma_detectado,
                'bandera': '🌐',
                'color': '#888'
            })

        st.markdown("---")
        st.markdown(f"<div class='bandera'>{info['bandera']}</div>", unsafe_allow_html=True)
        st.markdown(
            f"<div class='resultado' style='background-color:{info['color']}22; border: 2px solid {info['color']};'>"
            f"Idioma detectado: {info['nombre']}</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<div class='confianza'>Confianza: {confianza:.1f}%</div>",
            unsafe_allow_html=True
        )

        # Mostrar probabilidades de todos los idiomas
        st.markdown("---")
        st.markdown("**Probabilidades por idioma:**")

        probs_ordenadas = sorted(
            zip(clases, probabilidades),
            key=lambda x: x[1],
            reverse=True
        )

        for idioma, prob in probs_ordenadas:
            info_i = INFO_IDIOMAS.get(idioma, {'nombre': idioma, 'bandera': '🌐'})
            st.progress(
                float(prob),
                text=f"{info_i['bandera']} {info_i['nombre']}: {prob*100:.1f}%"
            )

# ─── Pie de pagina ────────────────────────────────────
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray; font-size:0.85em;'>"
    "Detector de Idiomas · Procesamiento de Lenguaje Natural · UPTC"
    "</div>",
    unsafe_allow_html=True
)
