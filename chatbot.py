# from flask import Flask
from dotenv import load_dotenv
from groq import Groq
import os
import gradio as gr
from transformers import pipeline
import numpy as np

transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")

def transcribe(audio):
    sr, y = audio
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))

    return transcriber({"sampling_rate": sr, "raw": y})["text"]  # type: ignore


demo = gr.Interface(
    transcribe,
    gr.Audio(sources=["microphone"], type="numpy"),
    "text",
)

demo.launch(share=True)


# load_dotenv()

# # app = Flask(__name__)

# # api_key = os.getenv('API_KEY')

# # Groq API key
# client = Groq(api_key = os.getenv('API_KEY'))

# model_engine = "llama3-8b-8192"

# conversation_history = []
# conversation_history.append({
#                     "role": "system",
#                     "content": "You are a friendly health advisor named Katniss. Your goal is to answer the patients' questions with medical, scientific advice. You are empathetic and knowledgeable. Guide them through the medical procedures if necessary as if you are a doctor or a nurse. Keep the response to 4 to 5 sentences if possible. When possible, provide additional links for the patients to gain more medical information relevant to their questions."
#                   })

# # generating model response
# def generate_response(prompt):
#     global conversation_history
#     conversation_history.append({"role":"user", "content":prompt})

#     response = client.chat.completions.create(
#         model=model_engine,
#         messages=conversation_history,
#         max_tokens=1024,
#         n = 1,
#         stop=None,
#         temperature=0.7,
#     )

#     health_advisor_response = response.choices[0].message.content

#     conversation_history.append({"role":"assistant", "content":health_advisor_response})

#     return health_advisor_response

# # gradio interface
# input_text = gr.Textbox(lines=7, label='Input')
# output_text = gr.Textbox(label="Output")
# gr.Interface(fn=generate_response, inputs=input_text, outputs=output_text, title="Chat with GPT-3", description="Enter to chat").launch(share=True)