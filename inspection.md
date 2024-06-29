# Inspection process aided by Google Gemini

inspection process aided by Gemini using Few-Shot and Chain-of-Thought prompting strategies based on https://github.com/Technical-Debt-Large-Scale/my_validation/blob/main/inspection_process.md

# A) Preparation:

## 1. Data Collection:
   
Gather the 226 critical issues identified in [Stage 3](https://github.com/Technical-Debt-Large-Scale/my_validation/blob/main/inspection_process.md#stage-3-data-preparation-involves-the-manual-selection-of-issues-to-be-inspected). Each issue should include:
-   Summary
-   Description
-   Comments
-   Label (if available from manual inspection - "Yes" or "No" for architectural impact)
    
## 2.  Gemini Model Selection

Choose a Gemini model suitable for text classification tasks. "gemini-1.0-pro-latest" is a good starting point.
    
## 3.  Prompt Development:
    
### Few-Shot Prompting:
-   Prepare a set of example issues with clear labels (architectural impact - Yes/No) for Gemini to learn from.
-   The examples should be similar to the 226 critical issues you have.
    
### Chain-of-Thought Prompting:

Develop a prompt that guides Gemini through its reasoning process. The prompt should include:
-   The issue summary, description, and comments (as input).
-   A clear instruction like "Analyze the provided information and determine if this issue has an architectural impact. Explain your reasoning." (This helps Gemini showcase its thought process).
 -   The desired output format ("Yes" or "No" with an explanation).
    
# B) Inspection Process:

## 1.  Manual Inspection (Optional): 

If you haven't already, manually inspect a subset of the 226 critical issues and assign labels ("Yes" or "No" for architectural impact). This data can be used for evaluation later.
    
## 2.  Gemini Inspection:
    
-   Use your Few-Shot prompt to train Gemini on the labeled examples.
-   Utilize the Chain-of-Thought prompt to guide Gemini through the inspection of each critical issue. The prompt should include the issue details (summary, description, comments) as input.
-   Gemini will analyze the information and provide a "Yes" or "No" output along with its reasoning for the architectural impact.
