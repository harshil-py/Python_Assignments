"""
13. Write a Python program to find if a given string starts with a
given character using Lambda.
Sample input: input_string = "Hello, World!", given_char = "H"
Sample Output: True
"""
input_string = "Hello, World!"
given_char = "H"

starts_with = lambda x: True if x.startswith(given_char) else False
print(starts_with(input_string))