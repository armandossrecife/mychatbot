import os
import google.generativeai as genai
from google.generativeai import GenerationConfig
import utils

### using gemini
def perform_gemini_inspection(issue_data, few_shot_prompts, model_name="gemini-1.0-pro-latest"):
  """
  Performs an inspection of an issue using Gemini with Few-Shot and Chain-of-Thought prompting.

  Args:
      issue_data (dict): Dictionary containing issue details (summary, description, comments).
      few_shot_prompts (str): Path to the file containing Few-Shot prompts.
      model_name (str, optional): Name of the Gemini model to use (default: "gemini-1.0-pro-latest").

  Returns:
      dict: Dictionary containing the issue details and Gemini's prediction (Yes/No with explanation).
  """
  # Configure generation
  generation_config = GenerationConfig(max_output_tokens=4096, temperature=0.1)
  genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
  model = genai.GenerativeModel(model_name, generation_config=generation_config)

  print('Wait for Train with Few-Shot prompts... ')

  # TODO: Falta criar um metodo para treinar o modelo basedo nos few-shots iniciais
  # Train with Few-Shot prompts
  conteudo_response_from_few_shot_prompts = []
  with open(few_shot_prompts, 'r') as prompt_file:
    prompts = prompt_file.read()
  response_from_few_shot_prompts = model.generate_content(prompts, stream=True)
  for chunk in response_from_few_shot_prompts:
    conteudo_response_from_few_shot_prompts.append(chunk)

  # Generate Chain-of-Thought prompt
  # Cria o prompt para cada issue fornecido
  try: 
    prompt = utils.generate_chain_of_thought_prompt(issue_data["summary"], issue_data["description"], issue_data["comments"])
  except Exception as ex: 
    print(f"Erro no generate_chain_of_thought_prompt: {str(ex)}")

  # TODO: tratar as seguintes exceptions: RequestError, InternalServerError, TimeoutError, ConnectionError
  print('Send prompt to Gemini and get response...')
  # TODO: garantir que o modelo vai analisar o issue e inferir Yes ou No para architecture issue
  # Send prompt to Gemini and get response
  response = model.generate_content(prompt, stream=True)
  conteudo_response = []
  answer = None
  explanation = None
  print("#"*50)
  print(f'Resultado da analise do issue {issue_data["summary"]}')
  for chunk in response:
    text = chunk.text.strip()
    conteudo_response.append(text)
    
  meu_texto = ""
  for item in conteudo_response:
    meu_texto = meu_texto + item
  
  if meu_texto.startswith("**Answer:**") or meu_texto.startswith("* Answer:"):
    if len(meu_texto.split("**Answer:**")) > 0: 
      answer = meu_texto.split("**Answer:**")[1]
      if answer: 
        answer = answer.split('\n')[0]
      else:
        answer = None
    if len(meu_texto.split("**Explanation:**\n")) > 0:
      explanation = meu_texto.split("**Explanation:**\n")[1]
      if explanation is None: 
        if len(meu_texto.split("* Explanation:")) > 0:
          explanation = meu_texto.split("* Explanation:")[1]
    
  # Combine results with issue data
  return {
      "summary": issue_data["summary"],
      "description": issue_data["description"],
      "comments": issue_data["comments"],
      "gemini_answer": answer,
      "gemini_explanation": explanation
  }