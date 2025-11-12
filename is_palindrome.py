# Python Challenge : Is it a Palindrome?
def is_palindrome(s):
    s = s.lower()
    reversed_text = s[::-1]
    return s == reversed_text

print(is_palindrome("racecar"))  
print(is_palindrome("hello"))     
print(is_palindrome("madam"))     

# Normalizing it (convert to lower case, keep only letters and numbers, check for palindrome)
def is_palindrome_clean(s):
    

    cleaned = ""  
    for char in s:
        if char.isalnum():  
            cleaned += char.lower()

    
    return cleaned == cleaned[::-1]



print(is_palindrome_clean("Race fast, safe car"))                    
print(is_palindrome_clean("A Toyota's a Toyota")) 
print(is_palindrome_clean("Hello, world!"))           

# Bonus : Print a message instead of True/False
def is_palindrome_message(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    if cleaned == cleaned[::-1]:
        return "Yes, it's a palindrome!"
    else:
        return "No, it's not a palindrome."


print(is_palindrome_message("Too hot to hoot"))
print(is_palindrome_message("Palindrome"))

