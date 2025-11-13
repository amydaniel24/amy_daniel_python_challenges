# LEVEL UP! Bonus Challenge
# Challenge: FizzBuzz with a Twist 


def fizzbuzz_twist():
    
    for num in range(1, 100):
        result = ""
        if num % 3 == 0:
            result += "Fizz"
        if num % 5 == 0:
            result += "Buzz"
        if num % 7 == 0:
            result += "Bang"

      
        print(result or num)


fizzbuzz_twist()
