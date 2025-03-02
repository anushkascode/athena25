import os
import google.generativeai as genai
from google.generativeai import types

def generate():
    genai.configure(api_key="AIzaSyCLC9Fza7aZUkttYBElrWvbkxhdNQiQr6M")

    model = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")

    prompt = """Generate a fun fact for the following task: Purchase clothing secondhand"""

    safety_settings = [
        types.SafetySettingDict(
            category="HARM_CATEGORY_HARASSMENT",
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
        types.SafetySettingDict(
            category="HARM_CATEGORY_HATE_SPEECH",
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
        types.SafetySettingDict(
            category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
        types.SafetySettingDict(
            category="HARM_CATEGORY_DANGEROUS_CONTENT",
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
    ]

    generation_config = types.GenerationConfig(
        temperature=1,
        top_p=0.95,
        top_k=64,
        max_output_tokens=8192,
    )

    system_instruction = """You are an expert on environmental science and sustainability. The users check off personal things they do that promote sustainability-- relating to topics from taking public transportation, to shopping locally or secondhand to reducing waste. Your task is to generate one-liner fun facts and analogies to encourage users who are taking steps towards a more sustainable lifestyle. The fun fact should be related to the task with creative, accessible-to-understand metrics/analogies for users to understand the impact of the task! Keep it to one or two sentences and include an accredited source, such as science journals and government websites."""

    response = model.generate_content(
        prompt,
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True
    )

    for chunk in response:
        print(chunk.text, end="")

generate() 