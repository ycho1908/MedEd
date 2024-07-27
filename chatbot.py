# from flask import Flask
from dotenv import load_dotenv
import os
import openai
import gradio as gr

load_dotenv()

# app = Flask(__name__)

api_key = os.getenv('API_KEY')

# openAI API key
openai.api_key = api_key

model_engine = "davinci"

# generating model response
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n = 1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# gradio interface
input_text = gr.inputs.Textbox(lines=7, label='Input')
output_text = gr.outputs.Textbox(label="Output")
gr.Interface(fn=generate_response, inputs=input_text, outputs=output_text, title="Chat with GPT-3", description="Enter to chat").launch()