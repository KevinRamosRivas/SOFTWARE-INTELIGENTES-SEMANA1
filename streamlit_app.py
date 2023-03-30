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

st.title("Chatboot de OpenAI GPT-3")

prompt = st.text_input("Ingresa tu mensaje:", key='prompt')
if st.button("Enviar", key='submit'):
  response = generar_respuesta(prompt)
  st.success(response)