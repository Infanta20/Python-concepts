from functools import reduce
num = [1,2,3,4,6,8,9,5]

# filter, map, reduce 

even = list(filter(lambda n: n %2 == 0, num))
print("Even numbers:", even)

double = list(map(lambda n : n * 2, even))  # it was take the list from even then it will double
print("Doubled even numbers:", double)

# def sum_it(a, b):
#     return a + b

# sum_it = lambda a, b : a + b
sum = reduce(lambda a, b : a + b, double)
print(sum)

#double = list(map(lambda n : n * 2, list(filter(lambda n: n %2 == 0, num)))) one line code
# print(double)


""""""""""""
# one-line expression that calculates the sum of cubes of all numbers in a list using map() and reduce()
num = [2,3,4]

cube = list(map(lambda n : n * n* n, num))
add = reduce(lambda a, b : a + b, num)
print("Sum of cubes:", cube)
print("Sum of numbers:", add)
