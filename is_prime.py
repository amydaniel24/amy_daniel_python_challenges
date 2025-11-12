# Python Challange: Check if a Number is Prime  

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(2))  
print(is_prime(11))  
print(is_prime(15))  
print(is_prime(1))   
print(is_prime(0))   

#Bonus functions 
import math

def is_prime_efficient(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime_efficient(2))    
print(is_prime_efficient(11))  
print(is_prime_efficient(15))  
print(is_prime_efficient(97))   

