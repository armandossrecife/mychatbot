import csv
import requests
import zipfile
import json

### Reads a CSV file containing issues and labels (separated by semicolons ;).
### Generates Few-Shot prompts for Gemini based on the data.
### Saves the generated prompts to a text file.
def create_few_shot_prompts(csv_file, label_column="label", output_file="prompts.txt"):
  """
  Reads a CSV file containing issues and labels, generates Few-Shot prompts for Gemini,
  and saves them to a text file.

  Args:
      csv_file (str): Path to the CSV file containing issues and labels.
      label_column (str, optional): Name of the column containing the label (default: "label").
      output_file (str, optional): Path to save the generated prompts (default: "prompts.txt").
  """
  with open(csv_file, 'r') as csvfile, open(output_file, 'w') as outfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
      summary = row["summary"]
      description = row["description"]
      # Assuming other details are in separate columns
      other_details = "..."  # Replace with how details are stored in your CSV
      label = row[label_column]

      # Construct the Few-Shot prompt
      prompt = f"**Issue:**\n* Summary: {summary}\n* Description: {description}\n* Other Details: {other_details}\n**Label:** {label}\n\n"
      outfile.write(prompt)

### Reads a CSV file containing issues and labels (separated by semicolons ;).
### Generates Few-Shot prompts for Gemini based on the data.
### Saves the generated prompts to a text file.
def create_few_shot_prompt_real_data(json_file, output_file="prompts.txt"):
  with open(json_file, 'r') as infile, open(output_file, 'w') as outfile:
    # Load the list of dictionaries from the file
    issues_groud_truth = json.load(infile)
    for row in issues_groud_truth:
      issue_id = row["issue_key"]
      summary = row["summary"]
      description = row["description"]
      label = row["architectural_impact_manual"]

      # Construct the Few-Shot prompt
      prompt = f"**Issue: {issue_id}**\n* Summary: {summary}\n* Description: {description}\n **Label:** {label}\n\n"
      outfile.write(prompt)

### Takes an issue's summary, description, and comments as input.
### Creates a Chain-of-Thought prompt guiding Gemini through its analysis.
### Returns the generated prompt string.
def generate_chain_of_thought_prompt(summary, description, comments):
  """
  Generates a Chain-of-Thought prompt for Gemini to analyze an issue and determine
  architectural impact.

  Args:
      summary (str): Summary of the issue.
      description (str): Description of the issue.
      comments (str): Comments associated with the issue.

  Returns:
      str: The generated Chain-of-Thought prompt.
  """
  prompt = f"""**Input:**

  * Summary: {summary}
  * Description: {description}
  * Comments: {comments}

  **Task:**

  Analyze the provided information and determine if this issue has an architectural impact. Explain your reasoning step-by-step. Consider aspects like code structure, maintainability, scalability, and potential design flaws.

  **Output:**

  * Answer: Yes or No (Does the issue have an architectural impact?)
  * Explanation: Explain your reasoning for the answer.
  """
  return prompt

# Dada uma url e um local de arquivo (destination) faz o download do conteudo da url no arquivo
def download_file(url, destination):
    try:
        response = requests.get(url) # Faz a requisicao do arquivo 
        response.raise_for_status()  # Verifica se houve algum erro na requisição
        conteudo = response.content  # Guarda o conteudo binario da resposta da requisicao
        # Coloca o conteudo da requisicao em um arquivo local 
        # Cria um novo arquivo e insere o conteudo neste arquivo
        with open(destination, mode='wb') as file:
            file.write(conteudo)
    except requests.exceptions.MissingSchema:
        # Caso seja uma excecao de url invalida
        print("URL inválida. Certifique-se de fornecer uma URL válida.")
        print("Download cancelado!")
        raise ValueError("URL inválida. Certifique-se de fornecer uma URL válida.")
    except requests.exceptions.ConnectionError:
        # Caso seja uma excecao de comunicacao de rede
        print(f"Erro na conexão!")
        print("Download cancelado!")
        raise ValueError("Erro na conexão!")
    except IOError: 
        # Caso aconteca um erro de IO do arquivo
        print(f"Arquivo {destination} inválido!")
        print("Download cancelado!")
        raise ValueError(f"Arquivo {destination} inválido!")

def unzip_file(my_file, path_to_unzip=None):
    try: 
        with zipfile.ZipFile(my_file, 'r') as zip_ref:
            zip_ref.extractall(path_to_unzip)
    except Exception as ex:
        raise ValueError(f"Erro ao descompactar: {str(ex)}")

def get_field_content(field_name, file_content):
    try:
        my_field = file_content.split(f"{field_name}:")[1]
        my_field = my_field.split('\n')[0]
        return my_field
    except Exception: 
        print(f"{field_name} não existe")

def convert_comment_to_text(comments_string):
  try: 
    comments_string = comments_string.split(": ")[-1]  # Assuming the colon and space separate the key-value pair
    comments_list = comments_string.split(",")
    comments = ""
    for comment in comments_list:
        comment = comment.replace("['", "")
        comment = comment.replace("']", "")
        comment = comment.replace(", '", " ")
        comment = comment.replace("'", "")
        comment = comment.replace("\\n", "\n")    
        comment = comment.replace("\\r", "\r")
        comments = comments + comment
    return comments
  except Exception as ex:
    print(f"Erro ao converter comment para texto: {str(ex)}")
    return None