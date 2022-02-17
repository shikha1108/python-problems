# A programming language has:
# 1. Keywords: for, def, return, if, else etc.
# 2. Identifiers: name, capital, capital_name, print, s etc
# 3. Literals: lucky

name = "lucky"


def capital(s):
    capital_name = s.upper() # upper(s)
    return capital_name

answer = capital(name)
print(answer)


def funny():
    print("Hello lucky")
    
funny()