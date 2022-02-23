numbers = [10, 20, 50]

def add_numbers(nums):
    add = 0
    for n in nums:
        result = add + n # evaluation happens from right to left
        add = result
    return add

print(add_numbers(numbers))


fruits = ["apple", "orange", "banana"]
def print_game(l):
    game = ""
    for f in l:
        result = game + f
        game = result
    return game

print(print_game(fruits))



if (print_game(fruits) == "appleorangebanana"):
    print("You win!")
else:
    print("You lose!")
    
# Data structure and Algorithms