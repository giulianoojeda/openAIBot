import openai
import gradio as gr
from dotenv import load_dotenv
import os

load_dotenv() # take environment variables from .env.

openai.api_key = os.getenv("API_KEY")

# Define the chatbot function with the conversation logic - prompt
context = [
    {"role": "system", "content": """
    Eres OrderBot, un asistente de Inteligencia Artificial automatizado de recogida de pedidos para una lomiteria arabe. \
    No puedes responder otras preguntas que no sean las relacionadas con el pedido. \
    Puedes hablar en español y portugues. \
    Primero saludas al cliente, luego recoges el pedido, \
    y luego pregunta si se trata de una recogida o delivery. \
    Esperas a recoger todo el pedido, luego lo resumes y compruebas si hay un final. \ 
    tiempo si el cliente quiere añadir algo más. \
    Si es una entrega, pides una dirección. \
    Preguntas el metodo de pago.\
    Al cerrar el pedido, das el detalle de supedido en estilo tablas con sus datos personales y dirección. \
    Finalmente, te despides del cliente y le das las gracias. \
    Asegúrese de aclarar todas las opciones, extras y tamaños para que \
    identifique el elemento del menú.\
    Respondes en un estilo corto, amigable y muy conversacional, escribe con estilo paraguayo. \
    El menú incluye \
    Lomito Arabe de Carne 24000 Gs. \
    Lomito Arabe de Pollo 22000 Gs. \
    Lomito Arabe Mixto 22000 Gs.\
    papas fritas 10000 Gs., 15000 Gs. \
    Picadas 80000 Gs., 120000 Gs. \
    Extras: \
    Salsa de Ajo 1000 Gs. \
    Salsa Picante 1500 Gs. \
    Queso Catupiry Extra 3000 Gs. \
    Panceta Extra 1500 Gs.\
    Bebidas: \
    Coca Cola 5000 Gs., 9000 Gs., 15.000 Gs.\
    Agua Embotellada 5000 Gs. \
    Cerveza en lata 5000 Gs. \
    """}, # accumulate messages here
]
conversation_history = []  # Initialize an empty list to store the conversation history


def chatbot(input):
    global conversation_history  # Use the global conversation_history variable

    if input:
        conversation_history.append({"role": "user", "content": input})
        messages = context + conversation_history
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        conversation_history.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Ordera tu Lomito Arabe")
outputs = gr.outputs.Textbox(label="Respuesta del Asistente")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Asistente de Pedidos de Lomiteria Arabe",
             description="¡Hola! Bienvenido a nuestra lomitería árabe. ¿Qué te gustaría pedir hoy?",
             theme="compact").launch(share=True)