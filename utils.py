import csv

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
      prompt = f"**Issue:**\n* Summary: {summary}\n* Description: {description}\n* Other Details: {other_details}\n\n**Label:** {label}\n\n"
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