
import dotenv, json
import os, requests

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from .prompts import based_prompt
from huggingface_hub import InferenceClient


dotenv.load_dotenv()
cronologia_chat = based_prompt

# def completion(prompt):
#     url = "https://api-inference.huggingface.co/models/Qwen/Qwen2.5-72B-Instruct"
#     response = requests.post(url=url, headers={'Authorization': f'Bearer {os.getenv("MyAPiKey")}'}, json={'inputs':prompt})
#     result = response.json()[0]['generated_text'][len(prompt):]
#     return(''.join(result.strip()))

def completion(prompt):
   
    client = InferenceClient(
        model='meta-llama/Meta-Llama-3.1-8B-Instruct',
        api_key=os.getenv("MyAPiKey")
    )
    response = client.chat_completion(
        messages=[
            {'role' : 'system', 'content' : based_prompt},
            {'role' : 'user', 'content' : prompt}
            
        ],
        stream=True,
        max_tokens=500
        
    )
    char = ''.join([char.choices[0].delta.content for char in response])
    return char
    # print(char)
  
def assistente_psicologo(user_token):
    
    
    print('richiestra in corso....')
    prompt = f'il mio messaggio: {user_token}\n{based_prompt}'
    return completion(prompt=prompt)



   