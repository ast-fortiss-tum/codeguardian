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
    log_true_pred_results
)


# Create a log file
if not os.path.exists('./logs'):
    os.makedirs('./logs')
    
# Configure logging
logging.basicConfig(filename='./logs/cwe_classification.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

languages = ['python', 'c', 'cpp', 'javascript', 'java']



def main(model_name, dataset_path):
    # System prompt: CWe-Sys2
    system_prompt = "You are an experienced developer who knows the security vulnerability very well."

    # General purpose prompt for vulnerability classification: CWE-UserZ
    general_prompt = """Classify the following code in CWE a category. 
    Output only one CWE tag in lowercase letters. Do not provide the full name of the CWE. 
    Respond with 'non-vul' if you determine the code is not vulnerable."""

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

    # This is for debugging...
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
            
            # count += 1
        # Record y_true and y_pred to the log file
        log_true_pred_results(y_true, y_pred, classification_type='cwe')
        # Calculate metrics
        accuracy, precision, recall, f1, cm = calculate_metrics_cwe(y_true, y_pred)
        output_matrics(accuracy, precision, recall, f1, cm, classification_type='cwe', round_up=True)

    # Make an excel file
    make_excel_file(results, model_name, classification_type='cwe')


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
    


