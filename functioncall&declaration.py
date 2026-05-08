def check_age(age):
    if age >= 18:
        print("Eligible for vote")
    else:
        print("Not Eligible")
        
age = int(input("enter the age:"))
result = check_age(age)