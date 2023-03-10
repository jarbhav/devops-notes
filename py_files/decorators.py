'''
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. 
Decorators are usually called before the definition of a function you want to decorate. 
'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

# Decorator example
@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())


# Multiple decorators example
    # Happens in order
@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'
print(say_hi())

## https://www.datacamp.com/tutorial/decorators-python