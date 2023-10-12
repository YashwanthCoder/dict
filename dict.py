def count_letters(input_string):
    letter_count = {}
    for char in input_string:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

# Test the function
input_string = "Hello, World!"
result = count_letters(input_string)
print(result)
