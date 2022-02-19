number1 = 40
number2 = 60

def add_number(num1, num2):
    addition = num1 + 5 + num2
    divide = addition / 4
    multiply = divide * 4
    return multiply
answer = (add_number(number1, number2))
print(answer)

#Algorithm: To reverse a list or array or queue
# 1. Create an empty list called reverse
# 2. Traverse the original list using for loop
# 3. While traversing, keep adding the current element to the head or beginning of the reverse list

fruits = ["apple", "orange", "banana", "grapes"]
fruits_reverse = []
 
def print_fruits(strs):
    for fruit in strs:
        fruits_reverse.insert(0, fruit)
        print(fruit)
        
print_fruits(fruits)        
print(fruits_reverse)
 