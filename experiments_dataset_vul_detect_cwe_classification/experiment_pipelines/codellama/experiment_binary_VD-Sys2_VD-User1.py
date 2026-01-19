import os
import argparse
import logging
import torch
import gc
from helper import (
    read_dataset, 
    calculate_metrics_binary, 
    make_excel_file, 
    classify_vulnerability, 
    setup_codellaama_model, 
    postprocess_response_binary,
    output_matrics
)


# if the logs directory does not exist, create it
if not os.path.exists('./logs'):
    os.makedirs('./logs')
# Configure logging
logging.basicConfig(filename='./logs/vul_binary_classification.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

languages = ['python', 'c', 'cpp', 'javascript', 'java']


# Main function
def main(model_name, dataset_path):
    # Set the role of the system: VD-Sys2
    system = "You are an experienced developer who knows the security vulnerability very well."
    # General purpose prompt for vulnerability classification: VD-User1
    general_prompt = """Classify the following code in vulnerable or not vulnerable. Output either only 'vulnerable' or 'not vulnerable'."""

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
            filtered_response = postprocess_response_binary(response)
            
            results.append({
                'true_label': item['true_label'],
                'language': item['language'],
                'vul_file_name': item['vul_file_name'],
                'vul_file_content': item['vul_file_content'],
                'vul_file_class': filtered_response
            })
            # Store the true and predicted label of the file
            if item['true_label'] == 'non-vul':
                y_true.append('not vulnerable')
            else:
                y_true.append('vulnerable')
            y_pred.append(filtered_response)

        ### Evaluate the model ###        
        # Record y_true and y_pred to the log file
        logging.info(f"y_true: {y_true}")
        logging.info(f"y_pred: {y_pred}") 
        
        # Calculate metrics
        accuracy, precision, recall, f1, cm = calculate_metrics_binary(y_true, y_pred)
        output_matrics(accuracy, precision, recall, f1, cm, classification_type='binary', round_up=True)

        
        # Clearing up the memory
        del tokenizer, model, data
        gc.collect()
        torch.cuda.empty_cache()

    # Save results to an excel file
    make_excel_file(results, model_name, classification_type='binary')
    

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


