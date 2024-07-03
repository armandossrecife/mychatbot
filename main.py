import utils
import automated_inspection
import json
import issues
        
def perform_create_few_shot_prompts(manual_inspecion="issues.csv"):
    try: 
        utils.create_few_shot_prompts(manual_inspecion)
    except Exception as ex:
        print(f"Erro: {str(ex)}")
        raise ValueError(ex)

def perform_create_few_shot_prompts_from_real_data(manual_inspecion="issues_ground_truth.json"):
    try: 
        utils.create_few_shot_prompt_real_data(manual_inspecion)
    except Exception as ex:
        print(f"Erro: perform_create_few_shot_prompts_from_real_data: {str(ex)}")
        raise ValueError(ex)


def perform_automated_inspection(filename="issues_to_inspection.json"):
    try: 
        # Open the JSON file for reading in read mode ('r')
        with open(filename, "r") as infile:
          # Load the list of dictionaries from the file
          critical_issues = json.load(infile)
        for issue in critical_issues:
            try: 
              inspection_result = automated_inspection.perform_gemini_inspection(issue, "prompts.txt")
            except Exception as ex: 
              print(f"Erro no issue {inspection_result['summary']}: {str(ex)}")
            if inspection_result['summary']: 
              print(f"Issue Summary: {inspection_result['summary']}")
            if inspection_result['gemini_answer']: 
              print(f"Gemini Answer (Architectural Issue): {inspection_result['gemini_answer'].upper()}")
            if inspection_result['gemini_explanation']:
              print(f"Explanation: {inspection_result['gemini_explanation']}")
            print("-"*50)
    except Exception as ex:
        print(f"Erro durante a inspeção automática dos issues: {str(ex)}")

def show_base_prompt(filename="prompts.txt"):
  try:
    with open(filename, mode="r") as f_prompt:
      conteudo = f_prompt.read()
    print(conteudo)
  except Exception as ex:
    print(f"Erro durante a exibição do prompt de base - {str(ex)}")
  pass

def show_issues_to_inspection(filename="issues_to_inspection.json"):
    try: 
      with open(filename, "r") as infile:
        critical_issues = json.load(infile)
      for i, issue in enumerate(critical_issues):
        try: 
          print(f"Seq: {i+1}")
          if issue["issue_id"]: 
            print(f"issue_id: {issue['issue_id']}")
          if issue["issue_type"]:
            print(f"issue_type: {issue['issue_type']}")
          if issue['summary']: 
            print(f"Issue Summary: {issue['summary']}")
        except Exception as ex: 
          print("-"*50)
    except Exception as ex:
      print(f"Erro durante a exibição dos issues: {str(ex)}")

try: 
    print("--- Creating the few shot prompts based on issues.csv ---")    
    # Contem os resultados da inspecao manual (Yes ou No para cada issue)
    print("O arquivo issues.csv contem os resultados (fragmento) da inspecao manual (Yes ou No para cada issue)")
    perform_create_few_shot_prompts(manual_inspecion="issues.csv")
    #print("O arquivo issues_ground_truth.json contem os resultados (completo) da inspecao manual (Yes ou No para cada issue)")
    #perform_create_few_shot_prompts_from_real_data()
    print("Few-Shot prompts generated and saved to prompts.txt")
    issues.generate_selected_issues(issues.filename)
    issues.convert_issues_to_json(issues.filename, path_arquivos_descompactados=issues.PATH_ARQUIVOS_DESCOMPACTADOS)
    print("--- Show the issue to be automatic inspection: ---")
    show_issues_to_inspection(filename="issues_to_inspection.json")
    print("$-$"*50)
    print("--- Show the prompts file base: ---")
    show_base_prompt(filename="prompts.txt")
    print("$-$"*50)
    print("--- Fazendo a inspeção automática dos issues selecionados... ---")
    perform_automated_inspection()
except Exception as ex:
    print(f"Erro: {str(ex)}")