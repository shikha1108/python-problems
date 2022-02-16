number1 = 30
number2 = 20


# A function/method has following parts:
# 1. It starts with def
# 2. After def, there is name of the function, name can not have space
# 3. After name, we have arguments inside paranthesis and they are separated by comma.
# 4. This line ends with colon
# 5. Next line has body of the function
# 6. Last part is return statement which returns the result
# Note: arguments are local variables
def add_number(num1, num2):
    
    return num1 + num2
    

# How to call a function
# Write the name of the function
# In paranthesis, we supply equal number of arguments and of same type
print(add_number(number1, number2))

