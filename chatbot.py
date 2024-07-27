# from flask import Flask
from dotenv import load_dotenv
from groq import Groq
import os
import gradio as gr

load_dotenv()

# app = Flask(__name__)

# api_key = os.getenv('API_KEY')

# Groq API key
client = Groq(api_key = os.getenv('API_KEY'))

model_engine = "llama3-8b-8192"

# generating model response
def generate_response(prompt):
    response = client.chat.completions.create(
        model=model_engine,
        messages=[{"role": "user",
                   "content": prompt}],
        max_tokens=1024,
        n = 1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message.content

# gradio interface
input_text = gr.Textbox(lines=7, label='Input')
output_text = gr.Textbox(label="Output")
gr.Interface(fn=generate_response, inputs=input_text, outputs=output_text, title="Chat with GPT-3", description="Enter to chat").launch(share=True)