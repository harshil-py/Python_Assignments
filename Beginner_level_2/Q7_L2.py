"""
7. Write a Python function that finds the median of a list of numbers. 
Sample Input: number_list = [7, 2, 5, 1, 9, 3] 
Sample Output: Median: 4.0
"""
number_list = [7, 2, 5, 1, 9, 3] 
def median_func(number_list):
    number_list.sort()
    n = len(number_list)
    if n % 2 == 0:
        return (number_list[n//2 - 1] + number_list[n//2]) / 2
    else:
        return number_list [n//2]


print(median_func(number_list))