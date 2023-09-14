# chainlit run langchain_integration.py -w
import os
import openai
import chainlit as cl
from dotenv import load_dotenv
from langchain import PromptTemplate, OpenAI, LLMChain

load_dotenv("chat.env")
openai_api_key = os.environ.get('OPENAI_API_KEY')
openai.api_key = openai_api_key
if openai_api_key is None:
    print("Error: No se encontró la variable de entorno OPENAI_API_KEY.")
else:
    print("La clave OPENAI_API_KEY ha sido importada correctamente.")


template = """Question: {question}

Answer: Lets think step by step."""

@cl.on_chat_start
def main():
    prompt = PromptTemplate(template = template, input_variables = ['question'])
    llm_chain = LLMChain(
        prompt = prompt,
        llm = OpenAI(temperature = 1 , streaming = True),
        verbose = True,
    )
    cl.user_session.set('llm_chain', llm_chain)

@cl.on_message
async def main(message : str):
    llm_chain = cl.user_session.get("llm_chain")
    
    res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])

    await cl.Message(content = res['text']).send()
