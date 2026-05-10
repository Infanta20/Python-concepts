#Decorators let you add extra behavior to a function, without changing the function's code.
#A decorator is a function that takes another function as input and returns a new function.

#the common functionality is applicable to multiple functions, we can use a decorator to avoid code duplication and keep our code short and clean.
def log_store(func):
    def wrapper(a,b):
        print("value:", a, "", b)
        result = func(a,b)
        print("Result:", result)
        return result
    return wrapper

# if we want to pass the multiple arguments to the function we can use * args example
def add_func(func):
    def wrapper(*args):
        print("values:", args)   # taking as a tuple
        result = func(*args)
        print("Result:", result)
        return result
    return wrapper


        
def decorator(func):
    def wrapper(a, b):
        if b > a:
            a, b = b, a
        return func(a, b)
    return wrapper
        
@decorator
@log_store
def sub(a,b):
    return a - b

@decorator
@log_store
def divide(a,b):
    return a / b

@add_func
def add(a,b,c):
    return a + b + c

# sub = decorator(sub)
# divide = decorator(divide)
print(sub(5,10))
print(divide(10,5))
print(add(5,10,7))
