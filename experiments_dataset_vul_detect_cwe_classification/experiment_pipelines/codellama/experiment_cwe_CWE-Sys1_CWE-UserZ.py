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
logging.basicConfig(filename='./logs/cwe_classification.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

languages = ['python', 'c', 'cpp', 'javascript', 'java']



def main(model_name, dataset_path):
    # Set the role of the system: CWE-Sys1
    system = """You are an AI vulnerability classifier that identifies CWE of a send code, if that code has a vulnerability. 
        You should respond with only one CWE. You don't have to respond with any other information except for one of the CWEs."""
    # General purpose prompt for vulnerability classification: CWE-UserZ
    general_prompt ="""Classify the following code in CWE a category. 
    Output only one CWE tag in lowercase letters. Do not provide the full name of the CWE. 
    Respond with 'non-vul' if you determine the code is not vulnerable."""
    
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
            # Classify the code in CWE category
            response = classify_vulnerability(general_prompt, item, system, tokenizer, model)
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
        log_true_pred_results(y_true, y_pred, classification_type='cwe')
        # Calculate metrics
        accuracy, precision, recall, f1, cm = calculate_metrics_cwe(y_true, y_pred)
        # Output metrics
        output_matrics(accuracy, precision, recall, f1, cm, classification_type='cwe', round_up=True)
        
        # Clearing up the memory
        del tokenizer, model, data
        gc.collect()
        torch.cuda.empty_cache()
    
    # Save results to an excel file
    make_excel_file(results, model_name, classification_type='cwe')



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
    


