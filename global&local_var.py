def print_values():
    x = 10  # local variable
    globals()['x'] = 20 # assigning a global variable
    print("Local value of x: ", x)
print_values()
print("Global value of x: ", x)

""""""""""""

a = 10 # global variable 
def func():
    a = 20 # local variable 
    print("inside func:", a)
func()
print("outside func:", a)
