"Module:- inheritance"

class School:

    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address

    def display_school(self):
        print(f"name of school : {self.name}")
        print(f"age of school : {self.age}")
        print(f"address of school : {self.address}")

class Student(School):

    def __init__(self,name,age,address,board):
        self.name = name
        self.age = age 
        self.address = address
        self.board = board

    def display_student(self):
        print(f"board of school : {self.board}")

def main():
    school = Student("Vidya Niketan school","since 1995","pune","MSOSAHS")
    school.display_school()
    school.display_student()

if __name__ == "__main__":
    main()

"Description: super() function"

class Employee():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_employee(self):
        print(f"name of the employee : {self.name}")
        print(f"age of the employee: {self.age}")

class Salary(Employee):
    def __init__(self, name, age,Salary):
        super().__init__(name, age)
        self.salary = Salary

    def display_salary(self):
        print(f"salary of employee: {self.salary}")

def main():
    employee = Salary("rohit",26,250000)
    print("----------------------")
    employee.display_employee()
    employee.display_salary()

if __name__ == "__main__":
    main()



