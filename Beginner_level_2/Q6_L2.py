"""
6. Write a Python program to check if a number is a power of two using recursion.
"""

def power_two(n):
    n = n/2
    if n == 2:
        return True
    elif n > 2:
        return power_two(n)
    else:
        return False
    
print(power_two(4))