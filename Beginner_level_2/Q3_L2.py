"""
3. Given an array of N integers and an integer K, find the number of pairs of elements in the array whose sum is equal to K. 
Sample Input: arr = [1, 2, 3, 4, 5], k = 6 
Sample Output: Pair count: 2
"""

arr = [1, 2, 3, 4, 5]
k = 6 
Pair_count = 0
for i in range(0,len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == k:
            Pair_count += 1

print(f'Pair_count: {Pair_count}')
