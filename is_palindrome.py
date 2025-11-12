# Python Challenge : Is it a Palindrome?
def is_palindrome(s):
    s = s.lower()
    reversed_text = s[::-1]
    return s == reversed_text

print(is_palindrome("racecar"))  
print(is_palindrome("hello"))     
print(is_palindrome("madam"))     