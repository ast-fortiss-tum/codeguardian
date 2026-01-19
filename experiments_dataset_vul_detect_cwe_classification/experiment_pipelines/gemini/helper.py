import glob 
import os
import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import pandas as pd
import logging
import datetime
from vertexai.generative_models import GenerationConfig


### Set up all CWE tags and their corresponding names ###
class_list = {
    'cwe-787': 'out-of-bounds write out-of-bounds-write',
    'cwe-79': "improper neutralization of input during web page generation cross-site scripting xss",
    'cwe-89': "improper neutralization of special elements used in an sql command sql injection",
    'cwe-416': 'use after free',
    'cwe-78': "improper neutralization of special elements used in an os command os command injection",
    'cwe-20': 'improper input validation',
    'cwe-125': 'out-of-bounds read out-of-bounds-read',
    'cwe-22': "improper limitation of a pathname to a restricted directory path traversal",
    'cwe-352': 'cross-site request forgery csrf',
    'cwe-434': 'unrestricted upload of file with dangerous type',
    'cwe-862': 'missing authorization',
    'cwe-476': 'null pointer dereference',
    'cwe-287': 'improper authentication',
    'cwe-190': 'integer overflow or wraparound',
    'cwe-502': 'deserialization of untrusted data',
    'cwe-77': "improper neutralization of special elements used in a command command injection",
    'cwe-119': 'improper restriction of operations within the bounds of a memory buffer',
    'cwe-798': 'use of hard-coded credentials',
    'cwe-918': 'server-side request forgery ssrf',
    'cwe-306': 'missing authentication for critical function',
    'cwe-362': "concurrent execution using shared resource with improper synchronization race condition",
    'cwe-269': 'improper privilege management',
    'cwe-94': "improper control of generation of code code injection",
    'cwe-863': 'incorrect authorization',
    'cwe-276': 'incorrect default permissions',
    'non-vul': 'not vulnerable'
}

list_cwe_names = [value.lower() for value in class_list.values()]

def load_cwe_db():
    with open("cwe-db.json", "r") as f:
        return json.load(f)

cwe_db = load_cwe_db()
########################################################

# Function to read and process files from the dataset
def read_dataset(dataset_path, language):
    # TODO: We need to read the dataset and process it to remove metadata.
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

def check_api_call_limit(count, limit=3):
    # Due to that GCP doesn't allow to invoke the API more than 5 times per minute, 
    # we have to wait for 61 seconds after 5 calls.
    if count % limit == 0 and count != 0:
        return True
    
    return False


# Function to remove metadata from code
def remove_metadata(code_content):
    # Split the code content into lines
    lines = code_content.split('\n')
    # Remove the first line assuming it's always metadata
    lines_without_metadata = lines[1:]

    return '\n'.join(lines_without_metadata)


# Function to classify vulnerability using Vertex AI PalM2
def classify_vulnerability(model, conversation):
    # Default parameters written in the documentation: https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text
    # Reason of why I didn't use ChatModel is "For text tasks that can be completed with one API response (without the need for continuous conversation), use the Text model."
    # https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-chat
    # Generation Config
    config = GenerationConfig(
        temperature=0.1
    )
    
    response = model.generate_content(
        [conversation],
        generation_config=config
    )

    logging.info("Input to Gemini API: {}".format(conversation))
    logging.info(f"Response from Gemini API: {response}")

    try:# Check if there are any candidates in the response
        return response.candidates[0].content.parts[0]._raw_part.text
    except:
        return 'non-content'


def run_binary_classification(model, general_prompt, item):    
    # Add the code snippet to the conversation
    input_prompt = f"{general_prompt}\n\n{item['vul_file_content']}"
    # Classify the code snippet as vulnerable or not vulnerable
    result = classify_vulnerability(model, input_prompt)
    
    # Remove spaces and new lines
    result = result.strip().replace('\n', '')
    
    # logging.info(f"Palm2 API called successfully for conversation: {input_prompt}")
    logging.info(f"True: {item['true_label']}, predicted: {result}")
    print(f"True: {item['true_label']}, predicted: {result}")
    
    return result


def postprocess_response_binary(response):
    # Filter the response to only keep "vulnerable" or "not vulnerable" -> This is due to CodeLlama producing redundant text...
    filtered_response = ""
    if "not vulnerable" in response.lower():
        filtered_response = "not vulnerable"
    elif "vulnerable" in response.lower():
        filtered_response = "vulnerable"
    else:
        # If the response doesn't contain "vulnerable" or "not vulnerable", return "non-vul"
        filtered_response = "not vulnerable"
        
    return filtered_response


def run_cwe_classification(model, general_prompt, item):
    # Add the code snippet to the conversation
    input_prompt = f"{general_prompt}\n\n{item['vul_file_content']}"
    # Classify the CWE of the code snippet
    result = classify_vulnerability(model, input_prompt)
    # Remove spaces and new lines
    result = result.strip().replace('\n', '')
    #logging.info(f"Palm2 API called successfully for conversation: {input_prompt}")
    logging.info(f"True: {item['true_label']}, predicted: {result}")
    print(f"True: {item['true_label']}, predicted: {result}")
    
    return result


# def retrieve_cwe_tag(classification):
#     # TODO: the output of the model varies, e.g., 'cwe-119' or 'cwe_119`, `os command injection`.
#     # We need to post-process the output to make it consistent.
    
#     for i, v in enumerate(list_cwe_names):
#         # Remove underscore or hyphen if present
#         v = v.strip().replace('_', ' ').replace('-', ' ')
#         v = v.lower()
#         if classification in v:
#             cwe_name = list(class_list.keys())[i]
#             # print("CWE tag:", cwe_name)
#             # logging.info(f"CWE tag: {cwe_name}")
#             return cwe_name
    
#     return 'cwe-unknown'

def retrieve_cwe_tag(classification):
    # Convert classification to a set of words
    classification_words = set(classification.lower().split())
    
    # Check in class_list
    for cwe_id, description in class_list.items():
        # Remove underscore or hyphen if present
        description = description.strip().replace('_', ' ').replace('-', ' ')
        # Convert description to a set of words
        description_words = set(description.lower().split())

        if classification_words.issubset(description_words):
            return cwe_id
    
    # Check in cwe_db
    for cwe_id, description in cwe_db.items():
        # Remove underscore or hyphen if present
        description = description.strip().replace('_', ' ').replace('-', ' ')
        # Convert description to a set of words
        description_words = set(description.lower().split())

        if classification_words.issubset(description_words):
            return cwe_id
    
    return 'cwe-unknown'


def postprocess_response_cwe(classification):
    # TODO: the output of the model varies, e.g., 'cwe-119' or 'cwe_119.
    # We need to post-process the output to make it consistent.
    
    # If the response contains "not vulnerable", return "not vulnerable"
    if "not vulnerable" in classification.lower() or 'non-vul' in classification.lower():
        return "non-vul"
    
    # Remove underscore or hyphen if present
    classification = classification.strip().replace('_', ' ').replace('-', ' ')
    classification = classification.lower()
    
    # if classification contains numbers, retrieve it and combine with 'cwe-'
    if any(char.isdigit() for char in classification):
        classification = 'cwe-' + ''.join(filter(str.isdigit, classification))
        print("Post-processed CWE tag:", classification)
        logging.info(f"Post-processed CWE tag: {classification}")
        
        return classification
    else:   
        classification = retrieve_cwe_tag(classification)
        print("Post-processed CWE tag:", classification)
        logging.info(f"Post-processed CWE tag: {classification}")
        
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


def log_true_pred_results(y_true, y_pred, classification_type='binary'):
    # Record y_true and y_pred to the log file
    logging.info("-------------------------------------") 
    logging.info(f"For {classification_type} task, y_true: {y_true}")
    logging.info(f"For {classification_type} task, y_pred: {y_pred}")
    logging.info("-------------------------------------") 


def output_matrics(accuracy, precision, recall, f1, cm, classification_type='binary', round_up='False'):
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
    # Create a directory to save the results
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