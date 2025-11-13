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
        return "Your password is STRONG as Hercules! "
    elif 3 <= score < 5:
        return "Ah, your password might not get hacked, it's MEDIUM strength. "
    else:
        return "Weak as WATER!!!!!! "


password = input("Enter a password: ")
print("Strength:", check_password_strength(password))
