"""Module:- create Variable"""
"""Description:- This program demonsrates how to create variable"""

Student_name = "Raj"
Student_age = 21
Student_Height = 5.2
is_student = True

print("\n-----Create variable-----")
print(f"Student Name: {Student_name}")
print(f"Student Age: {Student_age}")
print(f"Student Height: {Student_Height}")
print(f"Is Student?: {is_student}")

#Check datatypes
"""This program is to demonstrate datatypes of each variable"""
employee_name = "om"
employee_age = 27
employee_salary = 50000
is_employee = True

print('\n-----check datatypes-----')
print(f"employee name: {type(employee_name)}")
print(f"employee age: {type(employee_age)}")
print(f'employee salary: {type(employee_salary)}')
print(f"Is employee?: {type(is_employee)}")

#Typecasting
"""Datatype conversion program"""
 #Integer to Float

Number= 21
converted_number = float(Number)

print(f"\n----float to integer----")
print(f"original number: {Number}")
print(f"converted number is: {converted_number}")
print(f"data_type: {type(converted_number)}")

#float to integer
Number_1 = 23.0
Converted_number = int(Number_1)

print("\n-----float to integer-----")
print(f"original number: {Number_1}")
print(f"converted num: {Converted_number}")
print(f"data_type : {type(Converted_number)}")

#Integer to string
Student_ID = 101
Converted_String = str(Student_ID)

print('\n----Integer to string----')
print(f"Orignal Number : {Student_ID}")
print(f"Converted String = {Converted_String}")
print(f"Data Type: {type(Converted_String)}")