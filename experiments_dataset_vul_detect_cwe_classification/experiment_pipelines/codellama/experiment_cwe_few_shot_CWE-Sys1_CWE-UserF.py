'''
This script is used to classify CWE of a given code snippet using Meta CodeLlama model.
We will pass the list of top 25 CWEs to the model as a prompt (i.e., few-shot learning).
'''
import os
import torch
import argparse
import logging
import gc

from helper import (
    read_dataset, 
    calculate_metrics_cwe, 
    make_excel_file, 
    classify_vulnerability, 
    setup_codellaama_model, 
    postprocess_response_cwe,
    postprocess_cwe_hierarchy,
    output_matrics,
    log_true_pred_results
)



# if the logs directory does not exist, create it
if not os.path.exists('./logs'):
    os.makedirs('./logs')
# Configure logging
logging.basicConfig(filename='./logs/cwe_classification_few_shot.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

languages = ['python', 'c', 'cpp', 'javascript', 'java']



def main(model_name, dataset_path):
    # Set the role of the system: CWE-Sys1
    system = """You are an AI vulnerability classifier that identifies CWE of a send code, if that code has a vulnerability. 
        You should respond with only one CWE. You don't have to respond with any other information except for one of the CWEs."""
    # General purpose prompt for vulnerability classification: CWE-UserF    
    general_prompt = """
    Classify the following code in a CWE category. The code should have a vulnerability that corresponds to one of the top-25 CWEs below. Output only one CWE tag in lower letters. Do not provide the full name of the CWE. 
    Respond 'non-vul' if you think the code is not vulnerable. Below is the list of the top 25 CWEs:
    
    cwe-787: Out-of-bounds Write
    cwe-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
    cwe-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')
    cwe-416: Use After Free
    cwe-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
    cwe-20: Improper Input Validation
    cwe-125: Out-of-bounds Read
    cwe-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
    cwe-352: Cross-Site Request Forgery (CSRF)
    cwe-434: Unrestricted Upload of File with Dangerous Type
    cwe-862: Missing Authorization
    cwe-476: NULL Pointer Dereference
    cwe-287: Improper Authentication
    cwe-190: Integer Overflow or Wraparound
    cwe-502: Deserialization of Untrusted Data
    cwe-77: Improper Neutralization of Special Elements used in a Command ('Command Injection')
    cwe-119: Improper Restriction of Operations within the Bounds of a Memory Buffer
    cwe-798: Use of Hard-coded Credentials
    cwe-918: Server-Side Request Forgery (SSRF)
    cwe-306: Missing Authentication for Critical Function
    cwe-362: Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
    cwe-269: Improper Privilege Management
    cwe-94: Improper Control of Generation of Code ('Code Injection')
    cwe-863: Incorrect Authorization
    cwe-276: Incorrect Default Permissions.
    """
    
    # Classify each file and save results
    results = []

    # Traverse all languages stored in the dataset
    for l in languages:
        logging.info(f"##### Language: {l} #####")
        print(f"##### Language: {l} #####")
        # Setup the CodeLlama model -> we must setup the model for each language to avoid CUDA out of memory error...
        tokenizer, model = setup_codellaama_model(model_name)
        data = read_dataset(dataset_path, l)
        
        # Store the true and predicted label of the file
        y_true, y_pred = [], []
        
        for item in data:
            # Classify the code whether it's vulnerable or not
            response = classify_vulnerability(general_prompt, item, system, tokenizer, model)
            # Filter the response to only keep "vulnerable" or "not vulnerable" 
            filtered_response = postprocess_response_cwe(response)
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

        ### Evaluate the model ###        
        log_true_pred_results(y_true, y_pred, classification_type='cwe_few_shot')
        # Calculate metrics
        accuracy, precision, recall, f1, cm = calculate_metrics_cwe(y_true, y_pred)
        # Output metrics
        output_matrics(accuracy, precision, recall, f1, cm, classification_type='cwe_few_shot')
        
        # Clearing up the memory
        del tokenizer, model, data
        gc.collect()
        torch.cuda.empty_cache()

    # Save results to an excel file
    make_excel_file(results, model_name, classification_type='cwe_few_shot')


if __name__ == "__main__":
    # Let use input the model name as a command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", help="The model name to use for chat",
                        default="codellama/CodeLlama-7b-Instruct-hf")
    parser.add_argument("--dataset_name", help="The path to the dataset",
                        default="vul_dataset_mini_ver2")
    
    args = parser.parse_args()
    dataset_path = f"../../dataset/{args.dataset_name}"

    # Run main function
    main(args.model_name, dataset_path)
    


