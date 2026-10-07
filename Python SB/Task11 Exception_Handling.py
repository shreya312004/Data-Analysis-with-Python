"""Module:- Exception Handling"""
"""Description:- This Program Demonstrate the Operation of Exception Handling"""

try:
    N1 = int(input("enter th enumber: "))
    N2 = int(input("enter the number: "))

    result = N1/N2
    result_1 = N1+N2
    result_2 = N1*N2
    result_3 = N1-N2
    result_4 = N1**N2
    result_5 = N1//N2
    result_6 = N1%N2

except ZeroDivisionError:
    print('Cannot divide by zero.')

else:
    print("\n-------Arithmatic Operation--------")
    print(f"Division : {result}")
    print(f"Addition : {result_1}")
    print(f"Multiplication : {result_2}")
    print(f"Subtraction : {result_3}")
    print(f"Power of : {result_4}")
    print(f"Floor Division : {result_5}")
    print(f"Modulus : {result_6}")

finally:
    print('\nthe program has been executed successfully.')