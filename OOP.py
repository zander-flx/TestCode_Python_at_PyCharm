# class Student:
#     def __init__(self,name,course,year_level):
#         self.name = name
#         self.course = course
#         self.year_level = year_level
#
#     def display_info(self):
#         print("Student Name:",self.name)
#         print("Course:",self.course)
#         print("Year Level:",self.year_level)
#
# student1 = Student("Ana Reyes","Computer Engineering",2)
# student1.display_info()

# class Phone:
#     def __init__(self, pmodel):
#         self.model = pmodel
#
#     def show_model(self):
#         print("Phone model is: ",self.model)
#
# phone1 = Phone(input("Enter Phone Model: "))
# phone1.show_model()

#Encapsulation

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#     def deposit(self,amount):
#         self.__balance += amount
#     def withdraw(self,amount):
#         self.__balance -= amount
#     def show_balance(self):
#         print("Account Name: ",self.owner)
#         print("Balance: ",round(self.__balance,2))
#
# account1 = BankAccount(input("Enter Account Name: "), float(input("Enter Balance: ")))
# account1.deposit(float(input("Enter Deposit Amount: ")))
# account1.withdraw(float(input("Enter Withdraw Amount: ")))
# account1.show_balance()

#Inheritance

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def introduce(self):
#         print("Hello. My name is",self.name)
#
# class Profession(Person):
#     def teach(self):
#         print(self.name, "is teaching Python Programming")
#
# teacher1 = Profession(input("Enter Name: "))
# teacher1.introduce()
# teacher1.teach()

#Polymorphism

# class Dog:
#     @staticmethod
#     def sound():
#         print("The dog barks.")
#
# class Cat:
#     @staticmethod
#     def sound():
#         print("The cat meows.")
#
# dog1 = Dog()
# cat1 = Cat()
#
# dog1.sound()
# cat1.sound()

#Abstraction

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class GCashPayment(Payment):
    def pay(self,amount):
        print("Paid", amount, "using GCash")

payment1 = GCashPayment()
payment1.pay(500)

