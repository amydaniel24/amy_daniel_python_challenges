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



print(is_palindrome_clean("Racecar"))                    
print(is_palindrome_clean("A man a plan a canal Panama")) 
print(is_palindrome_clean("Hello, world!"))           


