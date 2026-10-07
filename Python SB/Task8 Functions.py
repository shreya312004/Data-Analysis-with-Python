"""Module : functions"""

Num_1 = int(input("enter the first number: "))
Num_2 = int(input("enter the second number: "))

def addition(Num_1,Num_2):
    total = Num_1 + Num_2
    return total

result = addition(Num_1,Num_2)

print("\n------addition of numbers------")
print(f'First Number : {Num_1}')
print(f"Second Number : {Num_2}")
print(f'sum of numbers : {result}')

"""Description : Display of Details through default argument"""

def student(name,age = 21):
    print("\n------basic details------")
    print(f'name of student : {name}')
    print(f' age of student : {age}')

student('Rohit')
student('Ritesh',25)

"""Description: Display of factorial"""

Number_1 = int(input('enter the number: '))
def factorial(Number):
    result = 1

    for value in range(1, Number + 1):
        result *= value
    return result 

Factorial_Result = factorial(Number_1)

print(f'factorial of {Number_1} : {Factorial_Result}')

"""Description: checking of prime numbers """

Number = int(input('enter any Number'))
def Prime(Number):
    if Number <= 1:
        return False
    return True

if Prime(Number):
    print(f'\n{Number} is a Prime Number')
else:
    print(f'\n{Number} is not a Prime Number')