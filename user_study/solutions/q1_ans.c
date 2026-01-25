// Correct answer: CWE-125: Out-of-bounds Read
// Source: From cwe-snippets, ./snippets_1/non-compliant/C/0025.c



int getValueFromArray(int *array, int len, int index) {
    int value;
    
    // check that the array index is less than the maximum
    // length of the array
    if (index < len && index >= 0) {
        // get the value at the specified index of the array
        value = array[index];
    }
    
    // if array index is invalid then output error message
    // and return value indicating error
    else {
        printf("Invalid array index\n");
        value = -1;
    }
    
    return value;
}