"Module:- file handling"
"description: - This Program Demonstrate the file handling operation"

with open("files.txt", "w") as file:
    file.write("Employee Name : Rohit\n")
    file.write("Employee Age : 27\n")
    file.write("Employee Department : IT\n")

print('-------written operation on file----------')
print('Data written successfully')

with open("files.txt", "r") as file:

    content = file.read()

print('\n--------Read Operation on file---------')
print('Employee details:')
print(content)

with open("files.txt", "a") as file:
    file.write('Employee Location : Pune\n')
    file.write('Employee Salary : 45000\n')

print('-----------Append Operation-----------')
print('Data appended successfully')

#import csv

#with open('employees.csv', 'r') as file:
  #  reader = csv.DictReader(file)
   # print('Employee Details:')

   # for employee in reader:
      #  print(f'Employee ID : {employee['Employee_ID']}')
       # print(f'name     : {employee['Name']}')
       # print(f'Department : {employee['Department']}')
        #print(f'Salary   : ₹{employee['Salary']}')
       # print('------------------------')