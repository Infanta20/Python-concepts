
from array import array
arr = array('i', [1, 2, 3, 4, 5])  #i refers to int typecode.
# arr2 = array('i', arr.tolist()) ||  #tolist method converts array to list 
arr2 = array(arr.typecode, (i for i in arr)) # this is more efficient way to create a new array from an existing one. 
# also we no need to mention the type of array 

# now we have the same elements in arr and arr2 but they are different objects in memory.
arr[1] = 10
print(arr)
print(arr2)


