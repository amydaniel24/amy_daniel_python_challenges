# Write a String and return it reversed using slicing
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))
print(reverse_string("Python"))

# Reversing the string with a for loop
def reverse_string_loop(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
print(reverse_string_loop("hello"))
print(reverse_string_loop("Python"))

# Bonus: Reverse a string while ignoring spaces and punctuation
def reverse_clean_verbose(text):
    cleaned = ""
    for char in text:
        if char.isalpha():
            cleaned += char
    print("Cleaned text:", cleaned)
    reversed_text = cleaned[::-1]
    print("Reversed text:", reversed_text)
    return reversed_text

reverse_clean_verbose("Hello, world!")