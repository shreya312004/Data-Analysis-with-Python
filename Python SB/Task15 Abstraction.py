"Module:- Abstraction"
"Description:- concept of abstraction"

from abc import ABC, abstractmethod
class Transport(ABC):
    def display(self):
        pass
class Vehicle(Transport):
    def display(self):
        print("this is an vehicle")

class Truck(Transport):
    def display(self):
        print("this is a truck")

class Railway(Transport):
    def display(self):
        print("this is a railway")

class Airway(Transport):
    def display(self):
        print("this is an airline")

def main():
    vehicle = Vehicle()
    truck = Truck()
    railway = Railway()
    airway = Airway()

    vehicle.display()
    truck.display()
    railway.display()
    airway.display()

if __name__ =="__main__":
    main()


