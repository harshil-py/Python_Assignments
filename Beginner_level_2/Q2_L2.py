"""
2. Create a function that takes a list and returns a new list with unique elements of the first list. 
Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5] 
Sample Output: list2 = [1, 2, 3, 4, 5]

"""
list1 = [1, 2, 2, 3, 4, 4, 5, 5] 
def unique_elements(list1):
    list2 = set(list1)
    return list(list2)

print(unique_elements(list1))
