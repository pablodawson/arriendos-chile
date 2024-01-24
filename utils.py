import os
from openai import OpenAI
import json

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)

prompt_txt = open("prompt.txt", "r").read()

def extraer_info_descripcion(descripcion):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt_txt + "\n" + descripcion
            }
        ],
        model="gpt-3.5-turbo",
    )
    text = chat_completion.choices[0].message.content
    
    return text

if __name__ == "__main__":
    text = extraer_info_descripcion("Casa en venta en La Reina, Santiago, Metropolitana de Santiago, Chile. 4 dormitorios.")