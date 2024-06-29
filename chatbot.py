# You need a Google API key to interact with Gemini's functionalities.
# Chave de API: configure a variavel de ambiente GOOGLE_API_KEY

# Google AI Python SDK for the Gemini API
# Install the library google-generativeai
# https://pypi.org/project/google-generativeai

import google.generativeai as genai
import os
import sys
from google.generativeai import GenerationConfig

qtd_tokens_enviados = []
qtd_tokens_recebidos = []

def configura_modelo(modelo='gemini-1.0-pro-latest', max_token=4096, my_temperature=0.1): 
    try:
        # Configure o acesso ao Google Gemini
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])        
        # Generation Config
        my_generation_config = GenerationConfig(max_output_tokens=max_token, temperature=my_temperature, top_p=1, top_k=32)
        # Defina o modelo de LLM
        model = genai.GenerativeModel(modelo, generation_config=my_generation_config)
    except Exception as ex:
        print(f"Erro na configuração do modelo: {str(ex)}")
        return False
    return model

def configura_chat(modelo:genai.GenerativeModel):
    try:
        chat = modelo.start_chat(history=[])
    except Exception as ex:
        print(f"Erro na configuração do chat: {str(ex)}")
        return False
    return chat

def pergunte_ao_gemini(chat_configurado:genai.ChatSession, prompt:str):
    try:        
        if chat_configurado:
            response = chat_configurado.send_message(prompt, stream=True)
            for pedaco in response: 
                print(pedaco.text)
        else:
            raise ValueError('O modelo não foi configurado corretamente')
    except Exception as ex:
        print(f"Erro: {str(ex)}")
        sys.exit(0)

def principal():    
    prompt = input('Qual é a pergunta? ')
    try: 
        modelo_configurado = configura_modelo()
        chat_configurado = configura_chat(modelo_configurado)
        while len(prompt) > 0: 
            print('Aguarde...')
            resposta = pergunte_ao_gemini(chat_configurado, prompt)  
            qtd_tokens_enviados.append(modelo_configurado.count_tokens(prompt))  
            print(resposta)
            qtd_tokens_recebidos.append(modelo_configurado.count_tokens(chat_configurado.history))
            prompt = input('Qual é a pergunta? ')
            if (not prompt) or (prompt.lower() == 'sair'):
                break
    except Exception as ex:
        print(f"Erro: {str(ex)}")

instrucoes = 'Digite sair para encerrar o programa'
print(instrucoes)
principal()
print(f"qtd_tokens_enviados: {qtd_tokens_enviados}")
print(f"qtd_tokens_recebidos: {qtd_tokens_recebidos}")