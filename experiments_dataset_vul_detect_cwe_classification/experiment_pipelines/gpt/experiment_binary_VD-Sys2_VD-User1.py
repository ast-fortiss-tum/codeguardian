import os
from openai import AzureOpenAI
import argparse
import logging
import dotenv

from helper import (
    read_dataset, 
    calculate_metrics_binary, 
    make_excel_file, 
    classify_vulnerability, 
    output_matrics,
    postprocess_response_binary
)

# Set up logging
if not os.path.exists('./logs'):
    os.makedirs('./logs')

# Configure logging
logging.basicConfig(filename='./logs/vul_binary_classification.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

languages = ['python', 'c', 'cpp', 'javascript', 'java']


# Main function
def main(model_name):
    # Set the role of the system: VD-Sys2
    conversation=[
        {"role": "system", 
         "content": "You are an experienced developer who knows the security vulnerability very well."}
    ]
    # General purpose prompt for vulnerability classification: VD-User1
    general_prompt = "Classify the following code in vulnerable or not vulnerable. Output either only 'vulnerable' or 'not vulnerable'."

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
        
        count = 0
        for item in data:
            conversation.append({"role": "user", "content": f"{general_prompt}\n{item['vul_file_content']}"})
            # print CWE label without breaking a new line
            print(f"{item['true_label']}: ", end='')
            classification = classify_vulnerability(conversation, client)
            # Filter the response to only keep "vulnerable" or "not vulnerable" 
            filtered_response = postprocess_response_binary(classification)
            
            results.append({
                'true_label': item['true_label'],
                'language': item['language'],
                'vul_file_name': item['vul_file_name'],
                'vul_file_content': item['vul_file_content'],
                'vul_binary_classification': filtered_response,
            })
            # Store the true and predicted label of the file
            if item['true_label'] == 'non-vul':
                y_true.append('not vulnerable')
            else:
                y_true.append('vulnerable')
            y_pred.append(filtered_response)
            # pop the last user message
            conversation.pop()
            
        # Record y_true and y_pred to the log file
        logging.info(f"y_true: {y_true}")
        logging.info(f"y_pred: {y_pred}") 
        
        # Calculate metrics
        accuracy, precision, recall, f1, cm = calculate_metrics_binary(y_true, y_pred)
        output_matrics(accuracy, precision, recall, f1, cm, classification_type='binary', round_up=True)

    # Make an excel file
    make_excel_file(results, model_name, classification_type='binary_r2_b1')



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
    


