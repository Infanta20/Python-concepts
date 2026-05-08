# Here the breaking point is working like insane for super understanding of loop work every time while running

i = 1

while i <= 5:   # this is the outer loop and it will run 5 times
    print("Infanta", end = " ") 
    j = 1 
    while j <= 1: # this is the inner loop and it will run 1 time for each iteration of the outer loop
        print("working in Capgemini", end = " ")
        j += 1 # this is the inner loop and it will run 1 time for each iteration of the outer loop
    print() # this is the outer loop and it will run 5 times in new line
    i += 1


# why this concept of while loop is when ever the time has change the date is not changed like 
#lets say today date is 26  the time is 9, it will go to 26th 10 26th 11 27th 0am 


""""""""""""""""""""""""
# print all even numbers from 1 to 10

n = int(input("Upto which number want to print: "))

j = 2
while j <= n:
    print(j, end=" ")
    j += 2

print("\nend")

"""""""""""""""""""""""""" 
data = [1, 2.5, "Infanta", True, [1, 2, 3], (4, 5, 6), {"name": "Infanta", "age": 25}]

i = 0
n = len(data)
while i< n:
    print(data[i])
    i += 1

# while loop is used when we don't know the number of iterations in advance, it will run until a certain condition is met.

# for loop is used when we know the number of iterations in advance, it will run for a specific number of times.

data = [1, 2.5, "Infanta", True, [1, 2, 3], (4, 5, 6), {"name": "Infanta", "age": 25}]

for value in data:
    print(value)
    
