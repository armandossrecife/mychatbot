# My Chatbot integrated to Google Gemini

Criação de um modelo automático (baseado no [Google Gemini](https://gemini.google.com)) para fazer inspeção de issues de projetos da [Apache foundation](https://www.apache.org/) para classificar se o issue tem algum tipo de impacto arquitetural ou não.

[Requisitos básicos da implementação](https://github.com/armandossrecife/mychatbot/blob/main/inspection.md)

[Instruções detalhadas dos prompts](https://github.com/armandossrecife/mychatbot/blob/main/instructions.txt)

- **chatbot.py**: conceitos básicos para fazer integração com o Gemini
- **myinspection.py**: implementa o processo automático basedo nos passos descrito nosso [processo de inspeção de issues](https://github.com/Technical-Debt-Large-Scale/my_validation/blob/main/inspection_process.md)
- **issues.csv**: representa a inspeção manual (Ground truth) de issues com problemas arquiteturais
- **utils.py**: modulo que contem as funções para ler o issues.csv e criar um prompt de cadeia para guiar o Gemini para a análise do issue.

Input: issues.csv e critical_issues
```python
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
```

Rode o programa principal: 
```bash
python3 myinspection.py
```

Output: resultados dos issues analisados pelo modelo
- Issue Summary: summary do issue 
- Gemini Answer (Architectural Issue):  YES ou NO
- Explanation: Justificativa do Architectural Issue
```bash
--- chain_of_thought_prompt ---
Few-Shot prompts generated and saved to prompts.txt
Wait for Train with Few-Shot prompts... 
Send prompt to Gemini and get response...
##################################################
Resultado da analise do issue Memory leak in core service
Issue Summary: Memory leak in core service
Gemini Answer (Architectural Issue):  YES
Explanation: 
The issue of a memory leak inthe core service has an architectural impact because it affects the overall design and structure of the system. A memory leak occurs when a program allocates memory but fails torelease it, leading to a gradual increase in memory usage over time. This can have several negative consequences:

* **Code Structure:** A memory leak can indicate a flaw in the code structure, such as improper memory management practices or missing cleanup routines. This can make the code difficult to maintain and debug.
* **Maintainability:** A memory leak can make it challenging to maintain the system, as it can be difficult to track down the source of the leak and implement a fix.
* **Scalability:** A memory leak can limit the scalability of the system, as it can lead to performance degradation and crashes as memory usage increases.
* **Design Flaws:** A memory leak can be a symptom of a deeper design flaw in the system, such as a lack of proper resource management or a failure to consider memory usage in the design.

Addressing a memory leak requires careful analysis of the code and system design to identify the root cause and implement asolution that prevents future leaks. This often involves refactoring code, implementing proper memory management techniques, and reviewing the overall design to ensure that memory usage is managed effectively.
--------------------------------------------------
Wait for Train with Few-Shot prompts... 
Send prompt to Gemini and get response...
##################################################
Resultado da analise do issue Database schema not optimized for frequent writes
Issue Summary: Database schema not optimized for frequent writes
Gemini Answer (Architectural Issue):  YES
Explanation: 
The issue has an architectural impact becausethe database schema is not optimized for frequent writes. This means that the database is not designed to handle the high volume of write operations efficiently. This can lead toperformance problems, such as slow write times and data integrity issues.

The following are some of the potential architectural impacts of this issue:

* **Code structure:** The code that interacts with the database may need to be modified to accommodate the new schema. This could involve changing the way that data is inserted, updated,and deleted.
* **Maintainability:** The new schema may be more difficult to maintain than the old schema. This could make it more difficult to make changes to the database in the future.
* **Scalability:** The new schema may not be as scalable as the old schema. This could make it difficult to handle increased traffic or data volumes in the future.
* **Design flaws:** The new schema may introduce design flaws that could lead to performance problems or data integrity issues.

It is important to note that the architectural impact of this issue will depend on the specific details of the database schema and the application that uses it.However, in general, any change to the database schema has the potential to impact the architecture of the application.
--------------------------------------------------
```

