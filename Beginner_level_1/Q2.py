""" 2. Write a program that accepts a string as input from the user and calculates the number of digits and letters.
Input: Hello123
Output: Alphabets: 5 & Number : 3
"""

user_in = list(input("please enter any alphabets or number : "))

Alphabets = 0
Number = 0
for i in user_in:
    if i.isalpha():
        Alphabets += 1
    else:
        Number +=1
        
output = f'Alphabets: {Alphabets} & Number : {Number}'
print(output)
