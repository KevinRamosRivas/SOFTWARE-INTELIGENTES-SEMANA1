import openai
import streamlit as st
# create an instance of the IMDb class





openai.api_key = "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"





def generar_respuesta(prompt):
    completions = openai.Completion.create (
        engine="text-davinci-003", #significa que estamos usando el modelo de lenguaje de Davinci
        prompt=prompt, #el texto que le pasamos al modelo
        max_tokens=1024, #el número máximo de tokens que queremos que genere el modelo
        n=1, #el número de respuestas que queremos que genere el modelo
        stop=None, #el texto que queremos que use el modelo para detener la generación de texto
        temperature=0.5, #la temperatura que queremos que use el modelo para generar el texto
        #la temperatura es un parámetro que controla la aleatoriedad de la respuesta generada.
    )

    message = completions.choices[0].text #obtenemos el texto generado por el modelo
    return message #devolvemos el texto generado por el modelo

st.title("IA que genera presentacion para perfil de linkedin")

# añadimos el logo de linkedin

st.image("https://play-lh.googleusercontent.com/kMofEFLjobZy_bCuaiDogzBcUT-dz3BBbOrIEjJ-hqOabjK8ieuevGe6wlTD15QzOqw", width=200)

name = st.text_input("Ingresa tu nombre:", key='nombre')

skills = st.text_input("Ingresa tus skills:", key='skills')

soft_skills = st.text_input("Ingresa tus soft skills:", key='soft_skills')

education = st.text_input("Ingresa tu nivel de educacion:", key='education')

goals = st.text_input("Ingresa tus metas profesionales:", key='goals')

# añadir un campo para los idiomas que habla

language = st.text_input("Ingresa los idiomas que hablas:", key='language')

prompt = "Haz un perfil de linkedin interesante sin exagerar para " + name + " con las siguientes skills: " + skills + " y soft skills: " + soft_skills + " y nivel de educacion: " + education + " y metas profesionales: " + goals + " y habla " + language + "."


if st.button("Enviar", key='submit'):
  response = generar_respuesta(prompt)
  st.success(response)