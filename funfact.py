import os
import random
import google.generativeai as genai
from google.generativeai import types

def generate(task):
    genai.configure(api_key="AIzaSyAQ2xC5R8EeeRxEYgeIIzrVKUTSedMX6j0")  # Replace with your actual API key

    model = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")

    # prompt = "Generate a fun fact for the following task: " + task.random.choice(["Plant a tree", "Buy Clothing Seconhand", "Limit your shower to under 10 minutes", "Purchase Produce from the local Farmer's Market", "Take Low-emission Transportation"])
    prompt = "Generate a fun fact for the following task: " + task
    
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

    system_instruction = """Your task is to generate one-liner fun facts and analogies to encourage users who are taking steps towards a more sustainable lifestyle. Only generate ONE FUN FACT please, the fun fact should always be on the SECOND LINE of the output after a header-- Example output: ("Here's a fun fact for the task: /n Fun Fact:"). You are an expert on environmental science and sustainability. The users check off personal things they do that promote sustainability-- relating to topics from taking public transportation, to shopping locally or secondhand to reducing waste. The fun fact should be related to the task with creative, accessible-to-understand metrics/analogies for users to understand the impact of the task! Keep it short and include an accredited source, such as science journals and government websites."""
    response = model.generate_content(
        prompt,
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=False  # Don't stream to process output easily
    )

    facts = response.text.split("\n")  # Split the generated text by double newlines
    
    if facts:
        # lines 2， 4， 6
        # rand = random.choice([2, 4])
        selected_fact = facts[0]
        selected_fact += facts[1]
        print("Selected Fact:", selected_fact)

        # Save the selected fact to a file
        with open("fun_fact.txt", "w", encoding="utf-8") as file:
            file.write(selected_fact)

        print("Fact saved to fun_fact.txt")

# generate()
