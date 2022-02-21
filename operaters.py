# Operators: +, -, *, /, %, =, ==, and, or, not etc


def plus(num1, num2):
    addition = num1 + num2 # = is called assignment operator
    return addition

# Test case
if (plus(40, 50) == 90): # == is called comparison operator
    print("plus Passed")
else:
    print("plus Failed")
    
    
def minus(num2, num3):
    substraction = num2 - num3
    return substraction

# Test case
if (minus(90, 50) == 40):
    print("minus Passed")
else:
    print("minus Failed")
    

def multiply(num1, num2):
    multi = num1* num2
    return multi

if (multiply(90, 50) == 4500):
    print("multiply Passed")
else:
    print("multiply Failed")
    
def modulo(num1, num2):
    mod = num1 % num2  # % is called modulo operator
    return mod

if (modulo(25, 6) == 1):
    print("modulo Passed")
else:
    print("modulo Failed") 


#If it does not rain and I have money then I will go for a movie.
# no rain -> True
# have money -> True
# watch movie -> True

# no rain -> False
# have money -> True
# watch movie -> False

# no rain -> True
# have money -> False
# watch movie -> False

# no rain -> False
# have money -> False
# watch movie -> False

#True and True = True

#opretors work on operands, (bool1,bool2 are operands) 

def anding(bool1, bool2):
    result = bool1 and bool2
    return result

if (anding(True, True) == True):
    print("anding Passed")
else:
    print("anding Failed") 
    
def oring(bool1,bool2):
    result = bool1 or bool2
    return result

if(oring(False, False) == True):
    print("oring passed")
else:
    print("oring failed")
    
def negation(bool1):
    result = not bool1
    return result

if(negation(False) == True):
    print("negation passed")
else:
    print("negation failed")
    
