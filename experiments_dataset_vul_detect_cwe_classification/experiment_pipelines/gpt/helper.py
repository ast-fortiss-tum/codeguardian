import glob 
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import pandas as pd
import logging
import datetime
import json
import re


class_list = {
    'cwe-787': 'out-of-bounds write',
    'cwe-79': "improper neutralization of input during web page generation ('cross-site scripting')",
    'cwe-89': "improper neutralization of special elements used in an sql command ('sql injection')",
    'cwe-416': 'use after free',
    'cwe-78': "improper neutralization of special elements used in an os command ('os command injection')",
    'cwe-20': 'improper input validation',
    'cwe-125': 'out-of-bounds read',
    'cwe-22': "improper limitation of a pathname to a restricted directory ('path traversal')",
    'cwe-352': 'cross-site request forgery (csrf)',
    'cwe-434': 'unrestricted upload of file with dangerous type',
    'cwe-862': 'missing authorization',
    'cwe-476': 'null pointer dereference',
    'cwe-287': 'improper authentication',
    'cwe-190': 'integer overflow or wraparound',
    'cwe-502': 'deserialization of untrusted data',
    'cwe-77': "improper neutralization of special elements used in a command ('command injection')",
    'cwe-119': 'improper restriction of operations within the bounds of a memory buffer',
    'cwe-798': 'use of hard-coded credentials',
    'cwe-918': 'server-side request forgery (ssrf)',
    'cwe-306': 'missing authentication for critical function',
    'cwe-362': "concurrent execution using shared resource with improper synchronization ('race condition')",
    'cwe-269': 'improper privilege management',
    'cwe-94': "improper control of generation of code ('code injection')",
    'cwe-863': 'incorrect authorization',
    'cwe-276': 'incorrect default permissions',
    'non-vul': 'not vulnerable'
}

list_cwe_names = [value.lower() for value in class_list.values()]


# Function to read and process files from the dataset
def read_dataset(dataset_path, language):
    # Top-25 CWEs + 1 non-vulnerable class
    data = []
    lang_path = os.path.join(dataset_path, language)
    for c_l in class_list:
        c_l_path = os.path.join(lang_path, c_l)
        # Finding all files that start with 'code_before' in cwe_path
        code_before_files = glob.glob(os.path.join(c_l_path, 'code_before*'))
        
        for file_path in code_before_files:
            with open(file_path, 'r') as file:
                code_before = file.read()
                # Process to remove metadata
                code_before = remove_metadata(code_before)
            
            # if code_before is empty, skip it
            if code_before == '':
                continue

            data.append({'true_label': c_l, 'language': language, 'vul_file_name': file_path, 'vul_file_content': code_before})
                
    return data


def calculate_metrics_binary(y_true, y_pred):
    # Labels
    labels = ['vulnerable', 'not vulnerable']

    # Calculate accuracy
    accuracy = accuracy_score(y_true, y_pred)
    # Calculate precision
    precision = precision_score(y_true, y_pred, labels=labels, average='binary', pos_label='vulnerable')
    # Calculate recall
    recall = recall_score(y_true, y_pred, labels=labels, average='binary', pos_label='vulnerable')
    # Calculate f1 score
    f1 = f1_score(y_true, y_pred, labels=labels, average='binary', pos_label='vulnerable')
    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    
    return accuracy, precision, recall, f1, cm

def calculate_metrics_cwe(y_true, y_pred):
    # Calculate accuracy
    accuracy = accuracy_score(y_true, y_pred)
    # Calculate precision
    precision = precision_score(y_true, y_pred, average='macro')
    # Calculate recall
    recall = recall_score(y_true, y_pred, average='macro')
    # Calculate f1 score
    f1 = f1_score(y_true, y_pred, average='macro')
    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    
    return accuracy, precision, recall, f1, cm


# Function to remove metadata from code
def remove_metadata(code_content):
    # Split the code content into lines
    lines = code_content.split('\n')
    # Remove the first line assuming it's always metadata
    lines_without_metadata = lines[1:]

    # return '\n'.join(lines_without_metadata)
    return '\n'.join(lines_without_metadata)


# Function to classify vulnerability using Azure OpenAI
def classify_vulnerability(conversation, client):
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_DEPLOYMENT_NAME"),
        messages=conversation,
        temperature=0.1,
    )
    # logging.info(f"OpenAI API called successfully for conversation: {conversation}")
    logging.info(f"Response: {response}")
    
    # print("response:", response.choices[0].message.content)

    return response.choices[0].message.content


def postprocess_response_binary(response):
    # Filter the response to only keep "vulnerable" or "not vulnerable" -> This is due to CodeLlama producing redundant text...
    filtered_response = ""
    if "not vulnerable" in response.lower():
        filtered_response = "not vulnerable"
    elif "vulnerable" in response.lower():
        filtered_response = "vulnerable"
    else:
        # If the response does not contain "vulnerable" or "not vulnerable", return "not vulnerable"
        # This expects that there is no obvious vulnerability in the code
        filtered_response = "not vulnerable"
    
    print("Filtered response:", filtered_response)
    logging.info(f"Filtered response: {filtered_response}")
    return filtered_response


def retrieve_cwe_tag(classification):
    # TODO: the output of the model varies, e.g., 'cwe-119' or 'cwe_119`, `os command injection`.
    # We need to post-process the output to make it consistent.
    
    for i, v in enumerate(list_cwe_names):
        if classification in v:
            cwe_name = list(class_list.keys())[i]
            # print("CWE tag:", cwe_name)
            # logging.info(f"CWE tag: {cwe_name}")
            return cwe_name
    
    return 'cwe-unknown'


def postprocess_response_cwe(classification):
    # If the response contains "not vulnerable", return "not vulnerable"
    if "not vulnerable" in classification.lower() or 'non-vul' in classification.lower():
        return "non-vul"
    
    # Remove underscore or hyphen if present
    classification = classification.strip().replace('_', ' ').replace('-', ' ')
    classification = classification.lower()
    
    # if classification contains numbers, retrieve it, remove leading zeros and combine with 'cwe-'
    if any(char.isdigit() for char in classification):
        digits = ''.join(filter(str.isdigit, classification))
        # Remove leading zeros by converting to int and back to string
        formatted_digits = str(int(digits))
        classification = 'cwe-' + formatted_digits
        # print("Post-processed CWE tag:", classification)
        logging.info(f"Post-processed CWE tag: {classification}")
        
        return classification
    else:   
        classification = retrieve_cwe_tag(classification)
        
    return classification


def postprocess_cwe_hierarchy(classification, true_label):
    # TODO: Some CWE tag has a hierarchy, such as CWE-77 is a parent of CWE-78, CWE-287 is a parent of CWE-295.
    # Thus, we need to post-process the output to avoid misclassification, e.g., CWE-78 can be also classified as CWE-77.
    
    # Return the original classification if it's the same as the true label
    if classification == true_label:
        return classification
    # Otherwise, check if the classification is a child of the true label
    else:
        with open('cwe-hierarchy.json', 'r') as file:
            hierarchy = json.load(file)

        for parent, children in hierarchy.items():
            if classification in children and parent == true_label:
                print("Found parent:", parent)
                logging.info(f"Found parent: {parent}")
                
                return parent
    
    # Return the original classification if no parent is found
    return classification
    

def output_matrics(accuracy, precision, recall, f1, cm, classification_type='binary', round_up=False):
    # Write results to the log file
    logging.info(f"Results for {classification_type} classification:")
    logging.info(f"Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1: {f1}")
    logging.info(f"Confusion matrix: {cm}")
    logging.info("-------------------------------------")
    # Print results to the console
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1: {f1}")
    print(f"Confusion matrix:")
    print(cm)
    
    if round_up:
        accuracy, precision, recall, f1 = round_up_metric(accuracy, precision, recall, f1)
        print("---Rounded up---")
        print(f"Accuracy: {accuracy}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
        print(f"F1: {f1}")
        logging.info(f"Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1: {f1}")
    

def make_excel_file(results, model_name, classification_type):
    # Create a directory to store the results
    if not os.path.exists('./artifacts'):
        os.makedirs('./artifacts')

    # Get the current date and time
    now = datetime.datetime.now()
    # Format the date and time as a string, e.g., '20231205_123456' for December 5, 2023, at 12:34:56
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    # Create a CSV file to save the results
    df = pd.DataFrame(results)
    # Save the file with a timestamp  
    df.to_excel(f'./artifacts/{classification_type}_classification_results_{model_name}_{timestamp}.xlsx', index=False)
    print(f"Results saved to Excel successfully: {classification_type}_classification_results_{model_name}_{timestamp}.xlsx")
    logging.info(f"Results saved to Excel successfully: {classification_type}_classification_results_{model_name}_{timestamp}.xlsx")
    
    
def round_up_metric(acc, precision, recall, f1):
    return round(acc, 4), round(precision, 4), round(recall, 4), round(f1, 4)