"Module:- Encapsulation"

class Employee:
    def __init__(self,name,age,salary):

        self.name = name
        self.age = age
        self._salary = salary

    def get_salary(self):

        return self._salary
        
    def set_salary(self,salary):

        if salary > 12000:
            self._salary = salary
        else: 
            print("invalid salary")

    def display(self):

        print("-------Employee Details-------")
        print(f"Name of employee : {self.name}")
        print(f"Age of employee : {self.age}")
        print(f"Salary of employee: {self._salary}")

def main():

    E1 = Employee("Ritesh",26,45000)
    E1.display()
    print(f"\nCurrent Salary: ₹{E1.get_salary()}")
    E1.set_salary(70000)
    print(f"Updated Salary : ₹{E1.get_salary()}")

if __name__  == "__main__":
    main()