# Description: Decorators With Arguments


def decorator(arg1, arg2):
    """Decorator with arguments"""

    def real_decorator(function):
        def wrapper(*args, **kwargs):
            print("Congratulations.  You decorated a function that does something with %s and %s" % (arg1, arg2))
            function(*args, **kwargs)

        return wrapper

    return real_decorator


# Call decorator with arguments
@decorator("arg1", "arg2")
def function_1(*args):
    print("Inside function_1")
    for arg in args:
        print(arg)
        

if __name__ == '__main__':
    function_1(1, 2, 3)

'''
Output:

Congratulations.  You decorated a function that does something with arg1 and arg2
Inside function_1
1
2
3

'''