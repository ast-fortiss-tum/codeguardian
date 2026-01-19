'''
This script is used to classify CWE of a given code snippet using Azure OpenAI.
We will pass the list of top 25 CWEs to the model as a prompt (i.e., few-shot learning).
'''

import os
from openai import AzureOpenAI
import dotenv
import argparse
import logging

from helper import (
    read_dataset, 
    calculate_metrics_cwe, 
    make_excel_file, 
    classify_vulnerability, 
    postprocess_response_cwe,
    postprocess_cwe_hierarchy,
    output_matrics
)

# Set up logging
if not os.path.exists('./logs'):
    os.makedirs('./logs')

# Configure logging
logging.basicConfig(filename='./logs/cwe_classification_few_shot.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

languages = ['python', 'c', 'cpp', 'javascript', 'java']


def main(model_name):
    # Set the role of the system: CWE-Sys2
    conversation = [
        {
            "role": "system",
            "content": """You are an experienced developer who knows the security vulnerability very well."""
        }
    ]
    
    # General purpose prompt for vulnerability classification in few-shot learning: CWE-UserF
    general_prompt = """
    Classify the following code in a CWE category. The code should have a vulnerability that corresponds to one of the top-25 CWEs below. Output only one CWE tag in lowercase letters. Do not provide the full name of the CWE. 
    Respond 'non-vul' if you think the code is not vulnerable. Below is the list of the top 25 CWEs:
        
    CWE-787: Out-of-bounds Write
    CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
    CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
    CWE-416: Use After Free
    CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
    CWE-20: Improper Input Validation
    CWE-125: Out-of-bounds Read
    CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
    CWE-352: Cross-Site Request Forgery (CSRF)
    CWE-434: Unrestricted Upload of File with Dangerous Type
    CWE-862: Missing Authorization
    CWE-476: NULL Pointer Dereference
    CWE-287: Improper Authentication
    CWE-190: Integer Overflow or Wraparound
    CWE-502: Deserialization of Untrusted Data
    CWE-77: Improper Neutralization of Special Elements used in a Command ('Command Injection')
    CWE-119: Improper Restriction of Operations within the Bounds of a Memory Buffer
    CWE-798: Use of Hard-coded Credentials
    CWE-918: Server-Side Request Forgery (SSRF)
    CWE-306: Missing Authentication for Critical Function
    CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
    CWE-269: Improper Privilege Management
    CWE-94: Improper Control of Generation of Code ('Code Injection')
    CWE-863: Incorrect Authorization
    CWE-276: Incorrect Default Permissions.
    """

    # Read dataset
    dataset_path = "../../dataset/vul_dataset_mini_ver2"
    # Classify each file and save results
    results = []
    
    # Traverse all languages stored in the dataset
    for l in languages:
        logging.info(f"##### Language: {l} #####")
        print(f"##### Language: {l} #####")
        data = read_dataset(dataset_path, l)
        
        # Store the true and predicted label of the file
        y_true, y_pred = [], []
        
        for item in data:
            conversation.append({"role": "user", "content": f"{general_prompt}\n{item['vul_file_content']}"})
            response = classify_vulnerability(conversation, client)
            filtered_response = postprocess_response_cwe(response)
            # print CWE label without breaking a new line
            print(f"{item['true_label']}: ", end='')
            print("Predicted: ", filtered_response)
            # Adjust classification based on CWE hierarchy to ensure accurate representation
            filtered_response = postprocess_cwe_hierarchy(filtered_response, item['true_label'])
            
            results.append({
                'true_label': item['true_label'],
                'language': item['language'],
                'vul_file_name': item['vul_file_name'],
                'vul_file_content': item['vul_file_content'],
                'vul_file_class': filtered_response
            })
            # Store the true and predicted label of the file
            y_true.append(item['true_label'])
            y_pred.append(filtered_response)
            # pop the last user message
            conversation.pop()

        # Record y_true and y_pred to the log file
        logging.info(f"y_true: {y_true}")
        logging.info(f"y_pred: {y_pred}") 
        
        # Calculate metrics
        accuracy, precision, recall, f1, cm = calculate_metrics_cwe(y_true, y_pred)
        output_matrics(accuracy, precision, recall, f1, cm, classification_type='cwe_few_shot', round_up=True)
        
    # Make an excel file
    make_excel_file(results, model_name, classification_type='cwe_few_shot')


if __name__ == "__main__":
    # Let use input the model name as a command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", help="The model name to use for chat",
                        default="gpt35-turbo")
    parser.add_argument("--platform", help="The platform to use for chat", default="azure")
    
    args = parser.parse_args()
    
    ### Set up Azure OpenAI client ###
    # Load environment variables from .env file based on the model name
    success = dotenv.load_dotenv(dotenv_path=f"../../credentials/.chat-azure-{args.model_name}.env")                             
    if not success:
        print("Could not read environment variables!")

    client = AzureOpenAI(
    azure_endpoint = os.getenv("OPENAI_API_BASE") , 
    api_key=os.getenv("OPENAI_API_KEY"),  
    api_version="2023-12-01-preview"
    )

    # Run main function
    main(args.model_name)
    


