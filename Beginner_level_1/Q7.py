"""
7. Write a Python program to check if a string is an anagram of another string.
string1 = "listen", string2 = "silent"
Output: True
"""
string_1 = list(input("Enter String 1: "))
string_2 = list(input("Enter String 2: "))

if sorted(string_1) == sorted(string_2):
    print(True)
else:
    print(False)

