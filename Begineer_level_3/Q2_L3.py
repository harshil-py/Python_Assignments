"""
2. Write a program to count the lines in a file “demo.txt”
"""

with open("demo.txt", "r") as f:
    lines = f.readlines()
    print(len(lines))