# Create the empty array and the pass the value there 
# ask the user for the size/value of an array 
# and run a loop from 0 to n:
# append that value to the empty array

from array import array


length = int(input("Enter the size of the array:"))

arr = array('i', [])  # 'i' refers to integer typecode
for i in range(length):
    element = int(input("Enter the value:"))
    arr.append(element)
print(list(arr))    