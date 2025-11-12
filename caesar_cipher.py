# Python Challenge : Caesar Cipher


def caesar_cipher(text, shift):
    result = ""  

    for char in text:
        if char.isalpha():  
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result

print(caesar_cipher("abc", 3))          
print(caesar_cipher("xyz", 2))           
print(caesar_cipher("Hello, World!", 5)) 

# Bonus: Decoding function
def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

encoded = caesar_cipher("Python Rocks!", 5)
print(encoded)                  
print(caesar_decipher(encoded, 5))  

# Bonus: User input

text = input("Enter a message to encode: ")
shift = int(input("Enter a shift value: "))
encoded = caesar_cipher(text, shift)
print("Encoded message:", encoded)
