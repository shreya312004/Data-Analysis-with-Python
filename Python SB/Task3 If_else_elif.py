"""Module:- If-else-elif"""
"""Description:- This Program Demonstrate the student Grade System."""

Name = input("enter name: ")
Marks= int(input("enter marks:"))

if Marks >=90:
    print(f" \n{Name}, you are passed with Grade A")
elif Marks >=70 and Marks <=90:
    print(f"\n{Name},you are passed with Grade B")
elif Marks >=60 and Marks <= 70:
    print(f"\n{Name}, you are passed with Grade D")
else:
    print(f'\n{Name}, you are Failed')