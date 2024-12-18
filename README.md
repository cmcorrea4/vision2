# 🤖 Analizador de Imágenes con IA

Esta aplicación de Streamlit permite analizar imágenes utilizando la API de OpenAI (GPT-4 Vision). Proporciona una interfaz amigable para cargar imágenes o capturarlas con la cámara web, y obtener descripciones detalladas del contenido utilizando inteligencia artificial.

## 📋 Características

- **Carga de Imágenes**: Soporte para formatos JPG, PNG y JPEG
- **Captura con Cámara**: Integración con cámara web para captura directa
- **Análisis con IA**: Descripción detallada usando GPT-4 Vision
- **Interfaz Intuitiva**: Diseño moderno y responsivo
- **Contexto Adicional**: Opción para agregar información complementaria
- **Diseño Responsivo**: Adaptable a diferentes tamaños de pantalla

## 🛠️ Requisitos Previos

- Python 3.8 o superior
- Una API key de OpenAI

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd analizador-imagenes
```

2. Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 📄 Archivo requirements.txt

```txt
streamlit
openai
Pillow
python-dotenv
```

## 🚀 Uso

1. Ejecuta la aplicación:
```bash
streamlit run app.py
```

2. Abre tu navegador web en `http://localhost:8501`

3. Ingresa tu API key de OpenAI en la barra lateral

4. Usa la aplicación de una de estas formas:
   - Sube una imagen usando el botón de carga
   - Captura una imagen usando la cámara web
   - Opcionalmente, añade contexto adicional
   - Haz clic en "Analizar Imagen"

## 🔑 Configuración de la API Key

La aplicación requiere una API key de OpenAI para funcionar. Puedes proporcionarla de dos formas:

1. **Directamente en la aplicación**: 
   - Ingresa la API key en el campo correspondiente en la barra lateral

2. **Variables de entorno**:
   - Crea un archivo `.env` en el directorio raíz
   - Añade tu API key:
     ```
     OPENAI_API_KEY=tu_api_key_aquí
     ```

## 🎯 Mejores Prácticas

- Usa imágenes claras y bien iluminadas para mejores resultados
- El tamaño máximo recomendado de imagen es 5MB
- Proporciona contexto adicional cuando sea relevante
- Asegúrate de tener una conexión a internet estable

## ⚠️ Limitaciones

- La aplicación requiere una conexión a internet activa
- El análisis está limitado por las capacidades del modelo GPT-4 Vision
- El tiempo de respuesta puede variar según la complejidad de la imagen

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`)
3. Realiza tus cambios
4. Haz commit de tus cambios (`git commit -am 'Añade nueva característica'`)
5. Push a la rama (`git push origin feature/nueva-caracteristica`)
6. Crea un Pull Request

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias, por favor:
1. Revisa los issues existentes
2. Crea un nuevo issue con una descripción detallada
3. Proporciona los pasos para reproducir el problema

---
Desarrollado con ❤️ usando Streamlit y OpenAI
