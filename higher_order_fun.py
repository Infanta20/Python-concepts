def square(num):
    return num * num
def cube(num):
    return num * num * num

# value = 6
# result = square(value)
# print(result)

def higher_order(num, operation): #here operation will take the function as an argument like square &cube 
    for i in num:
        result = operation(i)
        print(result)

num = [4,6,5]
higher_order(num, square)   
higher_order(num, cube)       

"""""""""""" 
#Write a Higher_order_function that takes a list of numbers and a function as input
# then applies that function to each number and prints the square of each element
# in the list
def Square(num):
    return num * num

def Cube(num):
    return num * num * num

def calculate(num, calculation, name):
    print(f"\n{name} results:")
    for i in num:
        result = calculation(i)
        print(result)

input_list = []
input_count = int(input("How many numbers do you want to input: "))

for i in range(input_count):
    input_num = int(input(f"Enter number {i + 1}: "))
    input_list.append(input_num)

calculate(input_list, Square, "Square")
calculate(input_list, Cube, "Cube")



