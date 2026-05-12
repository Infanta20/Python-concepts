#class has two components : 1. properties = variables (object)   2. methods = behaviour (functions)
# class ku ulla iruka variables and funcitons is called data members
#object is an instance(copy) of a class here object is refered as a details. class is like template, 
#without a object we cannot access the properties and methods of a class. we can create multiple objects for a class.

#before oops in python code:
# no_of_students = 50
# no_of_teachers = 5

# def classroom():
#     print("This is a classroom")  
# def teacher():
#     print("This is a teacher")

#after oops in python code:  #Bank
class Bank_Account:
    Customer_Name = "infa"
    Balance = 0
    account_number = 0

    def deposit(self):
        amount = int(input("Enter the amount to deposit:"))
        self.Balance = amount 

    def withdraw(self):
        amount = int(input("Enter the amount to withdraw:"))
        if self.Balance >= amount:
            self.Balance -= amount
        else:
            print("Insufficient balance")

Cus1 = Bank_Account 
print(Cus1.Customer_Name) #accessing the properties of the class using the object

cus2 = Bank_Account
cus2.Customer_Name = "Infanta"
print(cus2.Customer_Name)

cus3 = Bank_Account
cus3. Balance = 25000
cus3.account_number = 456789
print("Bank Balance:", cus3.Balance )
print("Account Number:", cus3.account_number )




