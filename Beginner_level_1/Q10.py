"""
10. Write a Python program to reverse the order of words in a givensentence.
Input_sentence = “Hello, World! Welcome to Pythonprogramming.”
Output after reverse = “programming. Python to Welcome World! Hello,”
"""

Input_sentence = r'" Hello, World! Welcome to Python programming. "'

a = Input_sentence.split(" ")
l = a[::-1]
out = " ".join(l)

print(f"Output after reverse = {out}")