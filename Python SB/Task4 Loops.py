"""module:- For Loop"""
"""Description: This prohram demonstrates basics for loops"""

i = 0
print("----for loop----")
for i in range(i,6):
    print(i)

x = 1
print("----while loop----")
while x < 5:
    print(x)

"""Description: Natural Numbers"""
Num = int(input('enter the number:'))
for Number in range(1, Num + 1):
    print(Number)

"""Description: Multiplication of table"""
Num = int(input('enter the number'))
count = 1
total = 0

while count <= Num:
    total += count
    count += 1

print(f'Sum of first{Num} numberws = {total}')

"""Description: Multiplication of table"""
Number_1 = int(input('enter the number:'))
print(f"\n Multiplication table: {Number_1}")
for i in range(1,11):
    print(f"{Number_1} x {i}= {Number_1* i}")

"""Description :- Pattern Printing using numbers"""
Num = int(input("enter any number:"))
for i in range(1, Number + 1):
    for j in range(1,i + 1):
        print(j, end="")
    print()

"""Description:- Factorial of an number"""
Number= int(input('enter any number'))
factorial = 1
for value in range(1, Number+1):
    factorial *= value
print(f'\nFactorial of {Number}: {factorial}')
vowels = ['a','e','i','o','u']
word = "python"
for letter in word.lower():
    if letter in vowels:
        print(letter)
    elif letter not in vowels:
        print(letter)
    else:
        print('not found')
