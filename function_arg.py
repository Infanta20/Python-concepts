# def add(num1 ,num2 = 0):   #default argument
#     return num1 + num2

# print(add(5))  #output: 5 we have pass the default value of num2


# def add(num1, *num2):   #variable length argument
#     sum = num1
#     for i in num2:
#         sum += i
#     return sum

# result = add(5, 10, 15, 20)  #output: 50 we have pass the variable length argument
# print(result)

# def person(name, age):
#     print("Name:", name)
#     print("Age:", age)
# person(age= 24, name = "Infanta")    #keyword argument
      


def person(name, **kwargs):   #keyword argument
    print("Name:", name)
    # print(kwargs) # returns a dictionary of the keyword arguments passed to the function
    for k,v in kwargs.items():
        print(k, ":", v)
person(age=25, name='Alice',city='Chennai', role="Engineer")





# def greet(name, msg='welcome to my website'):
#     print("hello", name,msg)
# greet('infanta')
# greet('vijai', 'Good to see you')


