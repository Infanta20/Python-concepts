
from array import array
arr = array('f', [9.2, 3.4, 5.6, -7.8])  #f refers to float typecode. similar to this we have int, double, char, etc.

#tolist method converts array to list
print(arr.tolist())

#iterating through array using for loop
for i in arr:
    if i < 0:  #it ignores negative numbers and
        continue
    print(i)


    

   