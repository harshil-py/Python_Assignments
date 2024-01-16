"""
11. Write a Python program to calculate the sum of digits of a given number until the sum becomes a single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24,
Again compute the sum of digits so that it can be reduced to
on single digit.
Final Output: 6
"""
def single_digit(num):
   sum_1 =  sum(map(int, str(num)))
   if sum_1 > 9:
      return single_digit(sum_1)
   return sum_1

print(single_digit(987))