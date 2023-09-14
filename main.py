# Command to run:
# chainlit run main.py -w
import os
import openai
import chainlit as cl
from dotenv import load_dotenv

load_dotenv("chat.env")  # asegúrate de que este archivo esté en el mismo directorio o proporciona la ruta completa
openai_api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = openai_api_key
if openai_api_key is None:
    print("Error: No se encontró la variable de entorno OPENAI_API_KEY.")
else:
    print("La clave OPENAI_API_KEY ha sido importada correctamente.")


@cl.on_message
async def main(message : str):
    response = openai.ChatCompletion.create(
        model = 'gpt-4',
        messages = [
            {'role': 'assistant','content': 'You are an assistant that is obsessed with legos'},
            {'role': 'user','content': message}
        ],
        temperature = 0.95
    )

    await cl.Message(content = f"{response['choices'][0]['message']['content']}",).send()

    