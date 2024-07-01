import utils
import automated_inspection
        
def perform_create_few_shot_prompts(manual_inspecion="issues.csv"):
    try: 
        utils.create_few_shot_prompts(manual_inspecion)
    except Exception as ex:
        print(f"Erro: {str(ex)}")
        raise ValueError(ex)

def perform_automated_inspection(critical_issues):
    try: 
        for issue in critical_issues:
            inspection_result = automated_inspection.perform_gemini_inspection(issue, "prompts.txt")
            print(f"Issue Summary: {inspection_result['summary']}")
            print(f"Gemini Answer (Architectural Issue): {inspection_result['gemini_answer'].upper()}")
            print(f"Explanation: {inspection_result['gemini_explanation']}")
            print("-"*50)
    except Exception as ex:
        print(f"Erro durante a inspeção automática dos issues: {str(ex)}")

critical_issues = [
  {
    "summary": "Memory leak in core service",
    "description": "The service responsible for handling user requests seems to be experiencing a memory leak. Memory usage keeps increasing over time, eventually leading to crashes and service disruptions.",
    "comments": "[User C] This issue has caused several outages in the past week. High priority to fix."
  },
  {
    "summary": "Database schema not optimized for frequent writes",
    "description": "The current database schema involves complex joins and aggregations, leading to slow performance when writing large amounts of data. This is causing bottlenecks in our data ingestion pipeline.",
    "comments": "[Tech Lead] We need to investigate database optimization techniques to improve write performance."
  }
]

try: 
    print("Creating the few shot prompts based on issues.csv")    
    print("O arquivo issues.csv contem os resultados da inspecao manual (Yes ou No para cada issue)")
    # Contem os resultados da inspecao manual (Yes ou No para cada issue)
    perform_create_few_shot_prompts(manual_inspecion="issues.csv")
    print("Few-Shot prompts generated and saved to prompts.txt")

    print("Fazendo a inspeção automática dos issues selecionados...")
    perform_automated_inspection(critical_issues)
except Exception as ex:
    print(f"Erro: {str(ex)}")