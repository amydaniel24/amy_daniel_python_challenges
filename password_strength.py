# LEVEL UP! Bonus Challenge
# Challenge: Password Strength Checker



def check_password_strength(password):
    
    length = len(password) >= 8
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    symbol = any(not c.isalnum() for c in password)

    score = sum([length, upper, lower, digit, symbol])

    if score == 5:
        return "Strong "
    elif 3 <= score < 5:
        return "Medium "
    else:
        return "Weak "


password = input("Enter a password: ")
print("Strength:", check_password_strength(password))
