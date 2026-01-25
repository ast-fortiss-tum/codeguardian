import pandas as pd

# Correct Answers and CWE Hierarchy
correct_answers = ['CWE-125', 'CWE-78', 'CWE-190', 'CWE-22', 'Not vulnerable', 'CWE-79']

cwe_hierarchy = {
    "cwe-787": ["cwe-121", "cwe-122", "cwe-123", "cwe-124"],
    "cwe-79": ["cwe-80", "cwe-81", "cwe-83", "cwe-84", "cwe-85", "cwe-86", "cwe-87", "cwe-88"],
    "cwe-89": ["cwe-564"],  
    "cwe-416": [],
    "cwe-78": [],
    "cwe-20": ["cwe-179", "cwe-622", "cwe-1173", "cwe-1284", "cwe-1285", "cwe-1286", "cwe-1287", "cwe-1288", "cwe-1289"],
    "cwe-125": ["cwe-126", "cwe-127"],
    "cwe-22": ["cwe-23", "cwe-36"],
    "cwe-352": [],
    "cwe-434": [],
    "cwe-862": ["cwe-425", "cwe-638", "cwe-939", "cwe-1314"],
    "cwe-476": [],
    "cwe-287": ["cwe-295", "cwe-306", "cwe-645", "cwe-1390"],
    "cwe-190": ["cwe-680"],
    "cwe-502": [],
    "cwe-77": ["cwe-78", "cwe-88", "cwe-624", "cwe-917"],
    "cwe-119": ["cwe-120", "cwe-125", "cwe-466", "cwe-786", "cwe-787", "cwe-788", "cwe-805", "cwe-822", "cwe-823", "cwe-824", "cwe-825"],
    "cwe-798": ["cwe-259", "cwe-321"],
    "cwe-918": [],
    "cwe-306": ["cwe-288", "cwe-322"],
    "cwe-362": ["cwe-364", "cwe-366", "cwe-367", "cwe-368", "cwe-421", "cwe-689", "cwe-1223", "cwe-1298"],
    "cwe-269": ["cwe-250", "cwe-266", "cwe-267", "cwe-268", "cwe=270", "cwe-271", "cwe-274", "cwe-648"],
    "cwe-94": ["cwe-95", "cwe-96", "cwe-1336"],
    "cwe-863": ["cwe-551", "cwe-639", "cwe-647", "cwe-804", "cwe-942", "cwe-1244"],
    "cwe-276": []
}


# Function to check if an answer matches the correct answer or its related CWEs
def check_answer(answer, correct_answer, cwe_hierarchy):
    # Check if the answer is not a string
    if type(answer) != str:
        return 0
    
    answer = answer.lower()
    correct_answer = correct_answer.lower()
    if answer == correct_answer:
        return 1
    else:
        for parent, children in cwe_hierarchy.items():
            if answer in children and parent == correct_answer:
                print("Found parent:", parent)
                
                return parent
        
    return 0

# Function to process each group's DataFrame
def process_group(df, correct_answers, cwe_hierarchy):
    new_df = df.copy()
    for col, correct in zip(df.columns, correct_answers):
        new_df[col] = df[col].apply(lambda x: check_answer(x, correct, cwe_hierarchy))
    return new_df


# Function to convert the custom time format to timedelta **without milliseconds**
def convert_to_timedelta(time_str):
    if pd.isna(time_str):
        return None
    parts = time_str.split('.')
    if len(parts) == 3:
        # Use only the minutes and seconds part
        new_time_str = parts[0] + ':' + parts[1]
        return pd.to_timedelta('00:' + new_time_str)
    return None
