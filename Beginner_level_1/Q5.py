"""
5. Write a Python program to find the factorial of a number using a for loop.
"""
num = int(input("Enter number to find factorial: "))

factorial = 1

if num < 0:
    print("Factorial of negative number can't be performed ")
elif num == 0:
    print("Factorial of zero is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print(f"factorial of {num} is {factorial}")
    