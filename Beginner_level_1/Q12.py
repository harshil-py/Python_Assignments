"""
12. Write a Python program to reverse a number using a while loop.
Sample Input: num = 12345
Sample Output: revnum = 54321
"""
num = 12345
revnum = 0

while num != 0:
    last_digit = num % 10
    revnum = revnum * 10 + last_digit
    num //= 10

print (f"revnum = {revnum}")