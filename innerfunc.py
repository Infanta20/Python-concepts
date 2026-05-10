def outer():
    print("This is outer function")
    
    def inner(num):
        print("Number passed in inner function:", num)
    
    return inner
something = outer() 
something(5) # it will give the address of inner function

""""""""""""
# where a function greet() defines another function message() inside it.
# inner function message("Welcome to python!")
# outer function should call the inner function

def greet():
    print("This is outer function")

    def message(msg):
        print("This is inner:", msg)
    message("Welcome to python!")
  
greet() 

