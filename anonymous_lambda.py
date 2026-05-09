# Anonymous lambda Function

#1 simple code
#before : def fun(num):
# return num * num
# result = fun(5)
# print(result)


fun = lambda num : num* num

result = fun(5)

print(result)

#2 add number

# f = lambda a, b = a + b
# result = f(5, 6)

# print(result)

#3 lambda function that takes a number as input & returns "Even" if 
#its even, otherwise returns "Odd".

num = int(input("Enter the number to check the even or odd:"))
isEven = lambda num: "Even" if num % 2 == 0 else "odd"
print(isEven(num))