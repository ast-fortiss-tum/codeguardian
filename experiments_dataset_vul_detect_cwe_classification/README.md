# Large Language Models for Secure Code Assessment: A Multi-Language Empirical Study

## Introduction

This repository contains the code for the paper "Large Language Models for Secure Code Assessment: A Multi-Language Empirical Study". Below is the description of the files and directories in this repository.

## Files and Directories

- dataset: Contains the dataset used in the paper. The dataset is a collection of five programming languages (Java, Python, JavaScript, C, and C++) with labeled vulnerabilities in the top-25 CWE categories. Our dataset has a total of 378 snippets. In addition, a jupyter notebook is provided to show how the dataset was created (`vul_dataset_analysis.ipynb`).

- experiment_pipelines: Contains the code for the experiment pipelines. The experiment pipelines are used to run five LLMs (GPT-3.5 Turbo, GPT-4 Turbo, GPT-4o, CodeLlama-7b, CodeLlama-13b, and Gemini 1.5 Pro). Each file contains a corresponding prompt set for the LLMs. 

- result_analysis: `excel_results' contains the results of the experiments in an excel file. Each folder has the results of the experiments for a specific prompt set.`analysis_all_average_macro_VD.ipynb` and `analysis_all_average_macro_CWE.ipynb` are jupyter notebooks that analyze the results of the experiments in vulnerability detection and CWE classification, respectively.

## Running the Experiments

- GPT models: Please make a file named `.chat-azure-{MODEL_NAME}.env` under "credentials" folder in the roo directory and add your credentials from Azure OpenAI Studio and its API, such as below:

```
OPENAI_API_KEY = "YOUR_API_KEY"
OPENAI_MODEL_NAME="YOUR_MODEL_NAME"
OPENAI_DEPLOYMENT_NAME = "YOUR_DEP_NAME"
OPENAI_API_BASE = https://YOUR_DEP_NAME.azure.com/
OPENAI_TYPE = "azure"
OPENAI_API_VERSION = "2022-12-01"
```

Used models with their corresponding versions are as follows:

* GPT-3.5 Turbo: version `1106`.
* GPT-4 Turbo: version `1106-Preview`.
* GPT-4o: version `2024-05-13`.



- CodeLlama models: Those have been run in Google Colab. Please make sure installing the following packages in the Colab environment:

```
pip install git+https://github.com/huggingface/transformers.git@main accelerate
```

- Gemini: Please make sure to set the environment variable GOOGLE_CLOUD_PROJECT to your Google Cloud project ID before running the experiments.

Used models with their corresponding version is as follows:

* Gemini 1.5 Pro: version `gemini-1.5-pro-001`.