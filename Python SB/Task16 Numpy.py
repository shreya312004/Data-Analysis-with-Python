'Module :- Numpy'
"Description :- use of arrays"

import numpy as np

list = np.array([10,20,30,40])
print('-----1D Array-----')
print(list)

list_1 = np.array([
    [10,20,25],
    [20,30,40]
])
print('\n----2D Array----')
print(list_1)

number = np.array([2,9,4,6,8,10,12,15,14])

print('\n-----indexing-----')
print(number[1])

print('\n----slicing-----')
print(number[1:4])
print(number [-2:])

print('\n-----Mathematical Operation-----')
print(f'addition of numbers : {number + 5}')
print(f'subtraction of numbers : {number - 2}')
print(f'multiplication of numbers : {number * 3}')
print(f'division of numbers : {number // 2}')

print('\n----Some Basic Operations-----')
print(f'Maximum number : {np.max(number)}')
print(f'Minimum number : {np.min(number)}')
print(f'total number: {np.sum(number)} ')
print(f'mean : {np.mean(number)}')
