"""
1. Write a Python program to find the common elements between two lists. 
Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8] 
Sample output: [4, 5]
"""
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8] 

def common_elements(l1,l2):
    l1_set = set(l1)
    l2_set = set(l2)

    if len(l1_set.intersection(l2_set)) > 0:
        return list(l1_set.intersection(l2_set))
    else:
        return "there are not any common elements"
    
print(common_elements(l1,l2))