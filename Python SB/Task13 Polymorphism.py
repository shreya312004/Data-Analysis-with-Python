"""Module : Polymorphism"""
"""Dscription :This Program demonstrates the concept of polymorphism"""

class Animal:

    def sound(self):
        print("there are different sounds of animals ")

class Dog(Animal):
    def sound(self):
        print('the dog sounds like bark bark')

class Cat(Animal):
    def sound(self):
        print("the cat sounds like meow meow")

class Cow(Animal):
    def sound(self):
        print("the cow sounds like mooo mooo")

def main():
    dog = Dog()
    cat = Cat()
    cow = Cow()

    dog.sound()
    cat.sound()
    cow.sound()

if __name__ == '__main__':
    main()
    