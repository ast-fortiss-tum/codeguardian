# User Study
This repository contains the code and used data for the user study.

## Folder / File Layout
- `README.md`: Overview of the user study (this file).
- `questions/`: Code snippets shown to participants (6 total).
- `solutions/`: Reference answers for the questions.
- `pre_questionnaire/`: Pre-study questionnaire data and analysis.
- `post_questionnaire/`: Post-study questionnaire data and analysis.
- `experiment/`: Experiment results and statistical analysis.

## Experiment Design
Participants first completed a pre-questionnaire about their **software development experience** and **cybersecurity knowledge**. Based on these responses, we split participants into two equal-sized groups using a random assignment (stratified by years of software development experience) and verified that the experience distributions were comparable between tghe two groups (see `./pre_questionnaire/group_analysis.ipynb`). The final group assignment is saved as `./pre_questionnaire/group_1.xlsx` (experimental) and `./pre_questionnaire/group_2.xlsx` (control).

1. Group1 (Experimental): Used the Code-Guardian extension to identify the most possible vulnerabilities in the code snippets.
2. Group2 (Control): Used any source from Internet except for LLM-based applications to identify the most possible vulnerabilities in the code snippets.

In the experiment, each participant worked through the same set of 6 vulnerability-identification tasks (`./questions/`). We collected task completion time and task completion accuracy as well as performed statistical analysis to compare the two groups (see `./experiment/statistical_analysis.ipynb`). Post-study responses are available under `./post_questionnaire/` which were asked only to Group1 (experimental) to collect feedback about the usability of the Code-Guardian extension.

## List of questions for the user study study

We have a total of 6 questions for the user study in `./questions/`. There are five questions that are based on the following languages: C, C++, Java, JavaScript, and Python. The last question is a placebo question that is based on Python.
The questions are as follows:

1. C
    1. CWE-125: Out-of-bounds Read
    2. Source: cwe-snippets, ./snippets_1/non-compliant/C/0025.c
2. C++
    1. CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')
    2. Source: Row 3 in ./dataset/CVEfixes/Analysis/results/C++/df_c++_cwe_78.xlsx
3. Java
    1. CWE-190: Integer Overflow or Wraparound
    2. Source: from cwe-snippets, snippets_90/non-compliant/Java/cwe-0190/byte_max_multiply_01.java0138.java
4. JavaScript
    1. CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')
    2. Source: Row 37 in ./dataset/CVEfixes/Analysis/results/JavaScript/df_javascript_cwe_22.xlsxs
5. Placebo (Python)
6. Python
    1. CWE-79 Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
    2. Source: Row 159 in ./dataset/CVEfixes/Analysis/results/Python/df_python_cwe_79.xlsx

## Statistical Analysis
The statistical analysis was performed in terms of the two variables: Task Completion Time and Task Completion Accuracy. The data was collected from the user study and the statistical analysis was performed using **the Mann-Whitney U test**.

## Results
The results of the user study are presented in the form of tables and graphs. The results are presented in the `./experiment/statistical_analysis.ipynb` notebook.