import os
import streamlit as st
import base64
from openai import OpenAI
import openai
from PIL import Image
import io
from streamlit_webrtc import webrtc_streamer
import cv2

# Función para codificar la imagen a base64
def encode_image(image_file):
    return base64.b64encode(image_file.getvalue()).decode("utf-8")

# Función para convertir imagen CV2 a bytes
def cv2_to_bytes(cv2_img):
    is_success, buffer = cv2.imencode(".jpg", cv2_img)
    if is_success:
        return io.BytesIO(buffer)
    return None

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Imagen AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS personalizado
st.markdown("""
    <style>
        .main > div {
            padding: 2rem;
            border-radius: 10px;
            background-color: #f8f9fa;
        }
        .stTitle {
            color: #1e88e5;
            font-size: 2.5rem !important;
            margin-bottom: 2rem !important;
        }
    </style>
""", unsafe_allow_html=True)

# Barra lateral con información
with st.sidebar:
    st.image('OIG4.jpg', width=200)
    st.title("📸 Guía de Uso")
    st.markdown("""
    ### Funcionalidades:
    1. **Carga de Imágenes** 📤
       - Sube imágenes en formato JPG, PNG o JPEG
       - Tamaño máximo recomendado: 5MB
    
    2. **Captura con Cámara** 📷
       - Usa tu cámara web para capturar imágenes
       - Asegúrate de tener buena iluminación
    
    3. **Análisis con IA** 🤖
       - Descripción detallada del contenido
       - Identificación de elementos clave
       
    4. **Contexto Adicional** ✍️
       - Añade información relevante para mejorar el análisis
    
    ### Requerimientos:
    - API Key de OpenAI
    - Conexión a internet estable
    """)
    
    # Input para la API key con diseño mejorado
    with st.expander("⚙️ Configuración API", expanded=False):
        ke = st.text_input('API Key de OpenAI', type="password")

# Configuración de la API
os.environ['OPENAI_API_KEY'] = ke if ke else ''
api_key = os.environ.get('OPENAI_API_KEY', '')

# Contenedor principal
st.title("🤖 Análisis Inteligente de Imágenes")

# Tabs para diferentes métodos de entrada
tab1, tab2 = st.tabs(["📤 Subir Imagen", "📷 Usar Cámara"])

with tab1:
    uploaded_file = st.file_uploader(
        "Arrastra o selecciona una imagen",
        type=["jpg", "png", "jpeg"],
        help="Formatos soportados: JPG, PNG, JPEG"
    )
    
    if uploaded_file:
        st.image(uploaded_file, caption="Imagen cargada", use_column_width=True)

with tab2:
    webrtc_ctx = webrtc_streamer(
        key="camera",
        video_processor_factory=None,
        media_stream_constraints={"video": True, "audio": False},
    )
    if webrtc_ctx.video_transformer:
        if st.button("📸 Capturar Imagen"):
            frame = webrtc_ctx.video_transformer.frame
            if frame is not None:
                uploaded_file = cv2_to_bytes(frame)
                st.image(frame, caption="Imagen capturada", use_column_width=True)

# Opciones adicionales
col1, col2 = st.columns(2)
with col1:
    show_details = st.toggle("✍️ Añadir contexto", value=False)
with col2:
    if show_details:
        additional_details = st.text_area(
            "Describe el contexto de la imagen:",
            placeholder="Ej: Esta imagen fue tomada durante...",
            disabled=not show_details
        )

# Botón de análisis con estilo mejorado
analyze_button = st.button(
    "🔍 Analizar Imagen",
    type="primary",
    use_container_width=True
)

# Lógica de análisis
if uploaded_file is not None and api_key and analyze_button:
    with st.spinner("🤖 Analizando imagen..."):
        try:
            base64_image = encode_image(uploaded_file)
            prompt_text = "Describe detalladamente lo que ves en la imagen en español. Incluye todos los elementos relevantes y su contexto."
            
            if show_details and additional_details:
                prompt_text += f"\n\nContexto adicional:\n{additional_details}"

            client = OpenAI(api_key=api_key)
            
            with st.status("Procesando...", expanded=True) as status:
                st.write("☁️ Conectando con OpenAI...")
                response = client.chat.completions.create(
                    model="gpt-4-vision-preview",
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": prompt_text},
                                {
                                    "type": "image_url",
                                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                                },
                            ],
                        }
                    ],
                    max_tokens=500,
                )
                status.update(label="✅ ¡Análisis completado!", state="complete")
                
            # Mostrar resultados
            st.success("Análisis completado con éxito")
            st.markdown("### 📝 Resultados del Análisis")
            st.markdown(response.choices[0].message.content)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
else:
    if not uploaded_file and analyze_button:
        st.warning("⚠️ Por favor, sube o captura una imagen primero.")
    if not api_key and analyze_button:
        st.warning("⚠️ Por favor, ingresa tu API key de OpenAI en la barra lateral.")
