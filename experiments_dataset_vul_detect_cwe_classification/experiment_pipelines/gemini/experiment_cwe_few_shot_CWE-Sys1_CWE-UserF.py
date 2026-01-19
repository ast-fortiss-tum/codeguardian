import os
import argparse
import logging
from vertexai.generative_models import GenerativeModel
import vertexai

from helper import (
    read_dataset,
    calculate_metrics_cwe,
    make_excel_file,
    output_matrics,
    run_cwe_classification,
    postprocess_response_cwe,
    postprocess_cwe_hierarchy,
    check_api_call_limit,
    log_true_pred_results
)

# Create a log file
if not os.path.exists('./logs'):
    os.makedirs('./logs')
    
# Configure logging
logging.basicConfig(filename='./logs/cwe_classification_few_shot.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

languages = ['python', 'c', 'cpp', 'javascript', 'java']



def main(model_name, dataset_path):
    # System prompt: CWE-Sys1
    system_prompt = """You are an AI vulnerability classifier that identifies CWE of a sent code, if that code has a vulnerability. 
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

    # Initialize the Vertex AI client
    # You must set the GOOGLE_CLOUD_PROJECT environment variable to your machine. 
    vertexai.init(project=os.environ['GOOGLE_CLOUD_PROJECT'], location="us-central1")
    logging.info(f"Using the model: {args.model_name}")
    model = GenerativeModel(
        model_name=args.model_name,
        system_instruction=[
            system_prompt
        ])
    
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
            # if check_api_call_limit(count, limit=4):
            #     print("Hits the limit of 5 calls per minute. Wait for 61 seconds...")
            #     time.sleep(61)
            
            cwe_result = run_cwe_classification(model, general_prompt, item)
            cwe_result = postprocess_response_cwe(cwe_result)
            # Adjust classification based on CWE hierarchy to ensure accurate representation
            cwe_result = postprocess_cwe_hierarchy(cwe_result, item['true_label'])
            
            logging.info(f"True: {item['true_label']}, predicted: {cwe_result}")
            results.append({
                'true_label': item['true_label'],
                'language': item['language'],
                'vul_file_name': item['vul_file_name'],
                'vul_file_content': item['vul_file_content'],
                'vul_binary_classification': cwe_result,
            })
            
            # Store the true and predicted label of the file
            y_true.append(item['true_label'])
            y_pred.append(cwe_result)
            
        # Record y_true and y_pred to the log file
        log_true_pred_results(y_true, y_pred, classification_type='cwe_few_shot')
        # Calculate metrics
        accuracy, precision, recall, f1, cm = calculate_metrics_cwe(y_true, y_pred)
        output_matrics (accuracy, precision, recall, f1, cm, classification_type='cwe_few_shot', round_up=True)
    
    # Make an excel file
    make_excel_file(results, model_name, classification_type='cwe_few_shot')


if __name__ == "__main__":
    # Let use input the model name as a command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", help="The model name to use for chat",
                        default="gemini-1.5-pro-001")
    parser.add_argument("--dataset_name", help="The path to the dataset",
                        default="vul_dataset_mini_ver2")
    
    args = parser.parse_args()
    dataset_path = f"../../dataset/{args.dataset_name}"

    # Run main function
    main(args.model_name, dataset_path)
    


