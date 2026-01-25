#include <stdio.h>
#include <stdlib.h>

int getValueFromArray(int *array, int len, int index) {
    int value;
    if (index < len) {
        value = array[index];
    } else {
        printf("Value is: %d\n", array[index]);
        value = -1;
    }
    return value;
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int len = sizeof(arr) / sizeof(arr[0]);
    
    printf("Array length: %d\n", len);
    
    int index;
    printf("Enter an index to retrieve the value: ");
    if (scanf("%d", &index) != 1) {
        printf("Invalid input! Please enter an integer.\n");
        return 1;
    }
    
    int value = getValueFromArray(arr, len, index);
    
    if (value != -1) {
        printf("Retrieved value: %d\n", value);
    }
    
    return 0;
}