import os
import utils
import json

MY_ISSUES_ZIP = "https://github.com/Technical-Debt-Large-Scale/my_validation/raw/main/cassandra/my_issues_to_inspection_cassandra.zip"
DIRETORIO_CORRENTE = os.getcwd()
filename = "my_issues_to_inspection_cassandra.zip"
DIRETORIO_ISSUES = os.path.join(DIRETORIO_CORRENTE,"downloads")
PATH_ARQUIVO_LOCAL = os.path.join(DIRETORIO_ISSUES,filename)
PATH_ARQUIVOS_DESCOMPACTADOS =  os.path.join(DIRETORIO_CORRENTE, "my_issues")

def convert_list_of_dict_in_json(data):
  try: 
    # Open the JSON file for writing in write mode ('w')
    with open("issues_to_inspection.json", "w") as outfile:
        # Use json.dump() to write the list of dictionaries to the file
        json.dump(data, outfile, indent=4)  # Optional: Add indentation for readability
  except Exception as ex:
    raise ValueError(f"Erro ao converter dados para json: {str(ex)}")

def generate_selected_issues(filename):
    print('Aguarde...')
    try:
        print(f'Fazendo o download do arquivo {filename}')
        utils.download_file(url=MY_ISSUES_ZIP, destination=PATH_ARQUIVO_LOCAL)
        print(f"Arquivo salvo em: {PATH_ARQUIVO_LOCAL}")
        print(f'Descompactando o arquivo {filename}')
        utils.unzip_file(PATH_ARQUIVO_LOCAL)
        print(f"Arquivo {filename} descompactado com sucesso")
    except Exception as ex:
        print(f"Erro: {str(ex)}")

def convert_issues_to_json(filename, path_arquivos_descompactados):
  # Lista de issues para serem inspecionados [dict1, dict2, .., dictN]
  issues_to_inspection = []
  print("Ler os arquivos")
  # Get list of files
  filenames = os.listdir(path_arquivos_descompactados)
  print(f"Lendo {len(filenames)} arquivos...")
  for filename in filenames:
    issue = {}
    file_path = os.path.join(path_arquivos_descompactados, filename)
    with open(file_path, 'r') as file:
      file_content = file.read()
      issue_type, summary, description, comments = None, None, None, None
      try: 
        issue_type = utils.get_field_content('issue_type', file_content)
        summary = utils.get_field_content('summary', file_content)
        description = utils.get_field_content('description', file_content)
        comments = utils.get_field_content('comments', file_content)
        issue["issue_id"] = filename
        issue["issue_type"] = issue_type
        issue["summary"] = summary
        issue["description"] = description
        issue["comments"] = comments
        issues_to_inspection.append(issue)
      except Exception as ex: 
        print(f"{filename} com problema em: {str(ex)}")      
  convert_list_of_dict_in_json(issues_to_inspection)
  print("List of dictionaries converted to JSON file: issues_to_inspection.json")