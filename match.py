# It is like the switch case in the other programming languages. It is used to compare a variable with multiple values and execute the corresponding block of code.

num = 7

match num:
    case 1:
        print("The number is one.")
    case 2:
        print("The number is two.")
    case 3:
        print("The number is three.")
    case _:
        print("Incorrect number")

""""""""""""""""""""
num = 15

match num % 3:
    case 0:
        print("Divisible by 3")
    case 1:
        print("The remainder is 1")
    case _:
        print("The remainder is 2")
