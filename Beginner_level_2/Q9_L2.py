"""
9. Write a Python program that executes an operation on a list 
and handles an IndexError exception if the index is out of range.
"""
lst = [1,2,3]
try:
    print(lst[5])
except IndexError as e:
    print(e)

