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
