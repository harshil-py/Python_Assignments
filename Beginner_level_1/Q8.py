"""
8. Write a Python program to calculate the LCM (Least Common Multiple) of two numbers.
number1 = 12, number2 = 18
LCM of 12 and 18 are: 36
"""
def LCM(x,y):
    if x > y :
        z = x
    else:
        z = y

    while True:
        if(z % x == 0) and (z % y == 0):
            lcm = z
            break
        z += 1
    return lcm

print(LCM(12, 18))