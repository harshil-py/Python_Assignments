"""
8. Write a Python function that counts the number of vowels in a given string. 
Sample Input: string = "Hello, World!" 
Sample Output: Number of vowels: 3
"""
vowels = ["a","e","i","o","u"]
in_string = "Hello, Word!"
def num_vowels(in_string):
    count = 0
    for i in in_string:
        if i in vowels:
            count += 1
    return count

vowel_count = num_vowels(in_string)
print(f"Number of vowels: {vowel_count}")
