import os
import utils

MY_ISSUES_ZIP = "https://github.com/Technical-Debt-Large-Scale/my_validation/raw/main/cassandra/my_issues_to_inspection_cassandra.zip"
DIRETORIO_CORRENTE = os.getcwd()
filename = "my_issues_to_inspection_cassandra.zip"
DIRETORIO_ISSUES = os.path.join(DIRETORIO_CORRENTE,"downloads")
PATH_ARQUIVO_LOCAL = os.path.join(DIRETORIO_ISSUES,filename)
PATH_ARQUIVOS_DESCOMPACTADOS =  os.path.join(DIRETORIO_CORRENTE, "my_issues")

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

print("Ler os arquivos")
# Get list of files
filenames = os.listdir(PATH_ARQUIVOS_DESCOMPACTADOS)
print(f"Lendo {len(filenames)} arquivos...")
for filename in filenames:
  file_path = os.path.join(PATH_ARQUIVOS_DESCOMPACTADOS, filename)
  with open(file_path, 'r') as file:
    file_content = file.read()
    issue_type, summary, description, comments = None, None, None, None
    try: 
        issue_type = utils.get_field_content('issue_type', file_content)
        summary = utils.get_field_content('summary', file_content)
        description = utils.get_field_content('description', file_content)
        comments = utils.get_field_content('comments', file_content)
    except Exception as ex: 
        print(f"Erro: {str(ex)}")
    print(f"File: {filename}\n issue_type: {issue_type} \n summary:{summary} \n description:{description} \n comments:{comments}")