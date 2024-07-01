import json
import utils

def read_result_ground_truth_inspection(filename="issues_ground_truth.json"):
    try: 
        contador = 0
        # Open the JSON file for reading in read mode ('r')
        with open(filename, "r") as infile:
          # Load the list of dictionaries from the file
          issues_groud_truth = json.load(infile)
        for issue in issues_groud_truth:
            print(f"issue_id: {issue['issue_key']}")
            print(f"issue_type: {issue['issue_type']}")
            print(f"summary: {issue['summary']}")
            print(f"description: {issue['description']}")
            print(f"architectural impact: {issue['architectural_impact_manual']}")
            print(f"comments: {issue['comments']}")
            if issue["comments"]:
                my_comment = utils.convert_comment_to_text(issue['comments'])
                print(f"my_comment: {my_comment}")
            print("---"*50)    
            contador += 1
    except Exception as ex:
        print(f"Erro durante a leitura dos issues ground truth: {str(ex)}")
    print(f"Quantidade de issues lidos: {contador}")

read_result_ground_truth_inspection(filename="issues_ground_truth.json")