"""Module: Classes"""
"""Description :- This Program Demonstrate the creation of class, object, attributes and method """

from symtable import Class


class School:

    def __init__(self):
      print("this is a student")
    
student = School()

"""Description :- This Program Demonstrate the creation of class, object, attributes and method """

class Employee:

    def __init__(self, Name, Age, Salary, Location):
        self.name = Name
        self.age = Age
        self.salary = Salary
        self.location = Location

    def display(self):
        print(f"Name of Employee : {self.name}")
        print(f"Age of Employee : {self.age}")
        print(f"Salary of Employee : {self.salary}")
        print(f"Location of Employee : {self.location}")

employee = Employee("Rohit",27,55000,"Pune")
employee.display()

"""Description :- This Program Demonstrate the Arithmetic Operation of two numbers"""

class Arithematic:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def display(self):

        addition = self.a + self.b
        subtraction = self.a - self.b
        multiplication = self.a * self.b
        division = self.a / self.b

        print(f"Num_1 : {self.a}")
        print(f"Num_2 : {self.b}")
        print(f"Addition : {addition}")
        print(f"Subtraction : {subtraction}")
        print(f"Multiplication : {multiplication}")
        print(f"Division : {division}")             


Operations = Arithematic(36,6)
Operations.display()    

    