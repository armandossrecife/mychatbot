# You need a Google API key to interact with Gemini's functionalities.
# Chave de API: configure a variavel de ambiente GOOGLE_API_KEY

# Google AI Python SDK for the Gemini API
# Install the library google-generativeai
# https://pypi.org/project/google-generativeai

import google.generativeai as genai
import os

def configura_modelo(modelo='gemini-1.0-pro-latest'): 
    try:
        # Configure o acesso ao Google Gemini
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        # Defina o modelo de LLM
        model = genai.GenerativeModel(modelo)
        return model
    except Exception as ex:
        print(f"Erro: {str(ex)}")
        return False

def pergunte_ao_gemini(prompt):
    try:
        modelo_configurado = configura_modelo()
        if modelo_configurado:
            response = modelo_configurado.generate_content(prompt, stream=True)
            for pedaco in response: 
                print(pedaco.text)
        else:
            raise ValueError('O modelo não foi configurado corretamente')
    except Exception as ex:
        print(f"Erro: {str(ex)}")

def principal():
    prompt = input('Qual é a pergunta? ')
    try: 
        while True: 
            print('Aguarde...')
            resposta = pergunte_ao_gemini(prompt)    
            print(resposta)
            prompt = input('Qual é a pergunta? ')
            if (not prompt) or (prompt.lower() == 'sair'):
                break
    except Exception as ex:
        print(f"Erro: {str(ex)}")

instrucoes = 'Digite sair para encerrar o programa'
print(instrucoes)
principal()