# multiple function calling.
# calling hierarchy: get_name() -> get_first_name() and get_last_name()
def get_first_name():
    return "Shikha"

def get_last_name():
    return "Yadav"

def get_name():
    first_name = get_first_name()
    last_name = get_last_name()
    name = first_name + " " + last_name
    return name

print(get_name())  