"""
9. Write a Python program to count the frequency of each elementin a list.
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
"""

Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
freq_count = {}
for i in Input_list:
    if i in freq_count:
        freq_count[i] += 1
    else:
        freq_count[i] = 1

print(f"Frequency count : {freq_count}")