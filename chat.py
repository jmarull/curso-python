from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)


def preguntar(prompt: str) -> str:
    respuesta = client.responses.create(
        model="gpt-5.5",
        instructions="""
        Responde siempre con ejemplos cortos.
        No escribas más de 150 palabras.
        """,
        input=prompt
    )

    return respuesta.output_text


def main():
    while True:

        pregunta = input("> ")

        if pregunta.lower() == "salir":
            break

        print()
        print(preguntar(pregunta))
        print()


if __name__ == "__main__":
    main()