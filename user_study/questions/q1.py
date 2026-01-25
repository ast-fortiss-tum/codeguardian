def count_character_case_sensitive(input_string, character):
    count = 0
    for char in input_string:
        if char == character:
            count += 1
    return count

def count_character_case_insensitive(input_string, character):
    count = 0
    input_string = input_string.lower()
    character = character.lower()
    for char in input_string:
        if char == character:
            count += 1
    return count

def main():
    str_input = input("Enter a string: ")
    check_character = input("Enter the character to count: ")
    case_sensitive = input("Count case-sensitively? (yes/no): ")
    reverse_string = input("Reverse string before counting? (yes/no): ")

    if len(check_character) != 1:
        print("Error: You must enter exactly one character to count.")
    else:
        if reverse_string.lower() == 'yes':
            str_input = str_input[::-1]

        if case_sensitive.lower() == 'yes':
            count = count_character_case_sensitive(str_input, check_character)
        else:
            count = count_character_case_insensitive(str_input, check_character)

        print(f"Number of '{check_character}' = {count}")

if __name__ == "__main__":
    main()

