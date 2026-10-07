"""Module: Sets"""
"""Description:- This program demonstrates the basic set opration"""

S1= {10,12,13,15}
S2 = {12,14,18,20}

print("\n---Original Set---")
print(f"Set 1:{S1}")
print(f"set 2 :{S2}")

print("\n-----Adding an element-----")
S1.add(19)
S2.add(16)
print(f"New set 1 after adding an element: {S1}")
print(f"New set 2 after adding an element: {S2}")

print('\n----Removing an element----')
S1.remove(19)
S2.remove(16)
print(f'New set 1 after removing an element: {S1}')
print(f"New set 2 after removing an element: {S2}")

print("\n----union operation----")
print(f"Union of sets: {S1.union(S2)}")

print("\n----Intersection operation----")
print(f'Intersection of sets : {S1.intersection(S2)}')

print("\n----Difference Operation----")
print(f'Difference in sets: {S1.difference(S2)}')


"Description : the key-value dictionary operations"

dict = {
    "ID": "Rohit",
    "Age": 21,
    "Location": "Pune"
}

print('\n----details in dictonary----')
print(f"Information : {dict}")

print("\n----key values in dictionaries----")
print(f'keys in dictionaries : {dict.keys()}')
print(f'values in dictionaries : {dict.values()}')

print('\n----adding to dictionary----')
dict["Salary"] = 45000
print(f'updated : {dict}')

print('\n-----updated dictionary----')
dict['Age'] = 26
print(f'updated : {dict}')

print('\n----delete operation----')
del dict["Salary"]
print(f'After Deletion the dictionary : {dict}')
