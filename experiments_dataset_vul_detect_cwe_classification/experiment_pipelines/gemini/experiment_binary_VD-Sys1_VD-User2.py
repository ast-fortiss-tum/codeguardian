import os
import datetime
import pandas as pd
import dotenv
import argparse
import logging
import time

from helper import read_dataset, calculate_metrics_binary, make_excel_file, run_binary_classification, output_matrics, check_api_call_limit, postprocess_response_binary, log_true_pred_results
from vertexai.generative_models import GenerativeModel
import vertexai



# If the logs directory does not exist, create it
if not os.path.exists('./logs'):
    os.makedirs('./logs')
# Configure logging
logging.basicConfig(filename='./logs/vul_binary_classification.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

languages = ['python', 'c', 'cpp', 'javascript', 'java']


def main(model_name, dataset_path, debug=False):
    # System prompt: VD-Sys1
    system_prompt = "You are an AI binary vulnerability classifier that identifies whether the provided code is vulnerable or not vulnerable. You should respond with either only 'vulnerable' or 'not vulnerable'."

    # General purpose prompt for vulnerability classification: VD-User2
    general_prompt = """Now you need to identify whether a code contains a vulnerability or not. If it has any potential vulnerability, output: 'vulnerable'. 
    Otherwise, output: 'not vulnerable'. You must respond with either 'vulnerable' or 'not vulnerable' only. The code is below."""
    
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

        count = 0
        for item in data:
            ### Debug mode ###
            count += 1
            if debug and count > 2:
                break

            result = run_binary_classification(model, general_prompt, item)
            filtered_result = postprocess_response_binary(result)
            
            results.append({
                'true_label': item['true_label'],
                'language': item['language'],
                'vul_file_name': item['vul_file_name'],
                'vul_file_content': item['vul_file_content'],
                'vul_binary_classification': filtered_result,
            })
            # Store the true and predicted label of the file
            if item['true_label'] == 'non-vul':
                y_true.append('not vulnerable')
            else:
                y_true.append('vulnerable')
            y_pred.append(filtered_result)
        
        # Record y_true and y_pred to the log file
        log_true_pred_results(y_true, y_pred, classification_type='binary')
        # Calculate metrics
        accuracy, precision, recall, f1, cm = calculate_metrics_binary(y_true, y_pred)
        output_matrics(accuracy, precision, recall, f1, cm, classification_type='binary', round_up=True)
    
    # Make an excel file
    make_excel_file(results, model_name, classification_type='binary_r1_b2')


if __name__ == "__main__":
    # Let use input the model name as a command line argument
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", help="The model name to use for chat",
                        default="gemini-1.5-pro-001")
    parser.add_argument("--dataset_name", help="The path to the dataset",
                        default="vul_dataset_mini_ver2")
    parser.add_argument("--debug", help="Run the program in debug mode", action="store_true")
    
    args = parser.parse_args()
    dataset_path = f"../../dataset/{args.dataset_name}"

    # Run main function
    main(args.model_name, dataset_path, args.debug)
    


