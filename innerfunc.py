def outer():
    print("This is outer function")
    
    def inner(num):
        print("Number passed in inner function:", num)
    
    return inner
something = outer() 
something(5) # it will give the address of inner function