import openai
import streamlit as st


# Establecemos API key de OpenAI
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Definimos la función que utiliza la API de OpenAI para generar una respuesta basada
# en el prompt que le pasamos
def generar_respuesta(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",  # modelo de lenguaje de OpenAI
        prompt=prompt,  # prompt que le pasamos al modelo
        max_tokens=1024,  # el número máximo de tokens que queremos que genere el modelo
        n=1,  # número de respuestas que queremos que genere el modelo
        stop=None,  # texto para detener la generación de texto
        temperature=0.5,  # controla la aleatoriedad de la respuesta generada
    )
    message = completions.choices[0].text  # obtenemos el texto generado por el modelo
    return message

# Creamos la interfaz de usuario utilizando Streamlit
st.title("IA que genera presentacion para perfil de linkedin")
st.text("Hola soy una IA que te ayuda a generar una presentacion para tu perfil de linkedin, a continuacion te pedire que me des algunos datos para generar tu presentacion.")

st.markdown("Integrantes:")
st.markdown("* Araujo Santillan, Pedro")
st.markdown("* Balceda Delgado, Adriana")
st.markdown("* Tocas Chipana, Nel")
st.markdown("* Ramos Rivas, Kevin")
st.markdown("* Zenobio Pariasca, Edgar")

# Añadimos el logo de Linkedin
st.image("https://play-lh.googleusercontent.com/kMofEFLjobZy_bCuaiDogzBcUT-dz3BBbOrIEjJ-hqOabjK8ieuevGe6wlTD15QzOqw", width=200)

# Creamos campos para que el usuario ingrese sus datos
name = st.text_input("Ingresa tu nombre:", key='nombre')
skills = st.text_input("Ingresa tus skills:", key='skills')
soft_skills = st.text_input("Ingresa tus soft skills:", key='soft_skills')
education = st.text_input("Ingresa tu nivel de educacion:", key='education')
goals = st.text_input("Ingresa tus metas profesionales:", key='goals')
language = st.text_input("Ingresa los idiomas que hablas:", key='language')

# Creamos el prompt a partir de los datos que el usuario ingresó
prompt = "Haz un perfil de LinkedIn interesante sin exagerar para " + name + " con las siguientes skills: " + skills + " y soft skills: " + soft_skills + " y nivel de educacion: " + education + " y metas profesionales: " + goals + " y habla " + language + "."

# Generamos la respuesta utilizando la API de OpenAI cuando el usuario 
# presiona el botón "Enviar"
if st.button("Enviar", key='submit'):
    response = generar_respuesta(prompt)
    st.success(response)
