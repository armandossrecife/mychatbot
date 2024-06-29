# You need a Google API key to interact with Gemini's functionalities.
# Chave de API: configure a variavel de ambiente GOOGLE_API_KEY

# Google AI Python SDK for the Gemini API
# Install the library google-generativeai
# https://pypi.org/project/google-generativeai

import google.generativeai as genai
import os
import sys

qtd_tokens_enviados = []
qtd_tokens_recebidos = []

def configura_modelo(modelo='gemini-1.0-pro-latest'): 
    try:
        # Configure o acesso ao Google Gemini
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        # Defina o modelo de LLM
        model = genai.GenerativeModel(modelo)
        chat = model.start_chat(history=[])
        return chat, model
    except Exception as ex:
        print(f"Erro: {str(ex)}")
        return False

def pergunte_ao_gemini(chat_configurado, prompt):
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
        chat_configurado, modelo_configurado = configura_modelo()
        while True: 
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