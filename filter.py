num = [1,24,35,46,67,87,97,56,34]

#def is_even(n):  #method: 1
# 	return n % 2 == 0
	
is_even = lambda n : n % 2 == 0  #method: 2

even = list(filter(is_even, num))
print(even)

#even in one line code method: 3
even = list(filter(lambda n: n %2 == 0, num))
print(even)

""""""""""""
# using filter() & lambda to extract all the numbers greater than 50 from the list

nums = [10,55,32, 75, 90, 41, 68]
extract = list(filter(lambda n : n > 50, nums))
print(extract)
