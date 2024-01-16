"""
4. Given an array of size N. The task is to rotate array by D elements towards right
Sample Input: arr = [1, 2, 3, 4, 5], D = 2 
Sample Output: arr after rotation = [4, 5, 1, 2, 3]
"""
D = 2
arr = [1,2,3,4,5]
new_arr = []

while D != 0:
    a = arr.pop()
    new_arr.append(a)
    D -= 1

new_arr.reverse()
new_arr.extend(arr)
print(new_arr)
