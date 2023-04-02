Integrantes:
* Araujo Santillan, Pedro
* Balceda Delgado, Adriana
* Tocas Chipana, Nel"
* Ramos Rivas, Kevin"
* Zenobio Pariasca, Edgar"


Este pequeño aplicativo consume la api de OpenAI y hace uso del modelo davinci, que sirve para la generación de texto.

Este aplicativo fue realizado con un framework llamado streamlit que permite crear aplicativos web de forma rápida y sencilla.
Requisitos:

* Python 3.6 o superior
* Pip
* Git


Pasos para poner en marcha:

1. Instalar streamlit( pip install streamlit) y openai(pip install openai)

2. Clonar el repositorio(git clone https://github.com/KevinRamosRivas/SOFTWARE-INTELIGENTES-SEMANA1.git)

3. Entrar a la carpeta del repositorio(cd SOFTWARE-INTELIGENTES-SEMANA1)

4. Ejecutar el comando "streamlit run streamlit_app.py"

5. Abrir el navegador en la dirección http://localhost:8501/

6. Listo, ya puedes usar el aplicativo.

Si es que el aplicativo no funciona, se puede probar en reemplazar la api_key por una propia
en la variable openai.api_key del archivo streamlit_app.py, por ejemplo 

# Establecemos API key de OpenAI
openai.api_key = "tu api key debe ir aqui"

