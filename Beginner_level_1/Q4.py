"""
4. Write a Python program to find the sum of all odd numbers between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25

"""
start = int(input("Enter a starting number: "))
stop =  int(input("Enter a stoping number: "))

odd_num = []
for i in range(start,stop):
    if i % 2 != 0:
        odd_num.append(i)
print(f"Sum of odd numbers : {sum(odd_num)}")

