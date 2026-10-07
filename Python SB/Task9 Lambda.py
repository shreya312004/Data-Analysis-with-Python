"""Module:- lambda functions"""
"""Description:- This Program Demonstrate the execution of lambda expression"""

int_1 = int(input("Enter the number: "))
int_2 = int(input("Enter the Number: "))

addition = lambda int_1,int_2: int_1 + int_2
result = addition(int_1,int_2)

print(f'addition : {result}')

"""Description:- This Program Demonstrate the execution of lambda using map function"""
numbers = [10,20,30,40,50]

result = list(map(lambda x: x*2,numbers))

print("\n--------Original List---------")
print(f'original list : {numbers}')

print("----------New List---------")
print(f'updated list : {result}')

"""Description:- This Program Demonstrate the execution of Lambda using filter function"""

Number = [2,3,4,5,6,7]
result_1 = list(filter(lambda X: X % 2 == 0,Number))

print("\n--------Original List---------")
print(f'original list : {Number}')

print("----------Even Numbers---------")
print(f'even numbers : {result_1}') 