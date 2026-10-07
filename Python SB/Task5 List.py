"""module :- list"""
"""Description :- this Program Demonstrates the list creation"""

List = ["mango",'bluebrerry','pineapple','Grapes']
print('------Indexing------')
print(f'First Element: {List[0]}')
print(f'Third Element: {List[3]}')
print(f'last element: {List[-1]}')

print('\n-----slicing-----')
print(f'first two elements: {List[:2]}')
print(f'Last three elements: {List[-3:]}')
print(f'middle element: {List[1:4]}')

print('\n----append-----')
List.append('Fruit')
print(f'append : {List}')

print("\n-----remove-----")
List.remove("Fruit")
print(f'remove: {List}')

"""Description:- Finding max and min value"""
marks = [60,65,70,77,80,88,90,94,97,98,93]
print('\n-----Student Marks-----')
print(f'Student Marks: {marks}')

Maximum = max(marks)
Minimum = min(marks)
Length = len(marks)

print(f'Maxium Marks: {Maximum}')
print(f'Minimum Marks: {Minimum}')
print(f'Total length : {Length}')