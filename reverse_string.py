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