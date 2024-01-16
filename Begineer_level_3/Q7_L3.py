"""
7. Write a program to construct a dictionary from the two lists
containing the names of students and their corresponding
subjects. The dictionary should map the students with their
respective subjects. Let’s see how to do this using for loops and
dictionary comprehension.
Input: [Sam, Alice, Mona] ,
[Commerce, Science, Computer]
Output: [Sam: Commerce, Alice: Science , Mona: Computer]
"""
l_name = ['Sam', 'Alice', 'Mona'] 
l_sub = ['Commerce', 'Science', 'Computer']

def dict_from_list(l_name,l_sub):
    dict_1 = {name:sub for name, sub in zip(l_name,l_sub)}
    return dict_1

print(dict_from_list(l_name, l_sub))