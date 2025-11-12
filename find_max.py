# Python Challenge: Find the Maximum Number in a List


def find_max(numbers):
   
    if not numbers:
        return "The list is empty."
    current_max = numbers[0]
    for num in numbers:
        if num > current_max:
            current_max = num  

    return current_max

print(find_max([4, 9, 1, 17, 2]))     
print(find_max([-5, -9, -2, -12]))   
print(find_max([42]))                 
print(find_max([]))                  

# Return the maximum number and its index
def find_max_with_index(numbers):
    if not numbers:
        return None, None
    
    max_value = numbers[0]
    max_index = 0

    for i in range(len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
            max_index = i

    return max_value, max_index

print(find_max_with_index([4, 9, 1, 17, 2]))  
print(find_max_with_index([-5, -9, -2, -12])) 

# Return it using a while loop
def find_max_while(numbers):
    if not numbers:
        return None

    i = 0
    current_max = numbers[0]

    while i < len(numbers):
        if numbers[i] > current_max:
            current_max = numbers[i]
        i += 1

    return current_max
print(find_max_while([3, 8, 2, 10, 6]))  

