"""
9. Given an input string, write a function that returns the run
length encoded string for the input string.
For Example:
Input: wwwwaaadebbbbbw
Output: w4a3d1e1b5w1

"""
str_in = "wwwwaaadebbbbbw"

def run_length(str_in):
    count = 0
    character = ''
    chatacter = ''
    previous_char = str_in[0]
    result = ''
    length = len(str_in) 
    
    i = 0
    while (i != length ):
        chatacter = str_in[i]
        
        if previous_char == chatacter :
            count = count + 1
        else :
            result = result + previous_char + str(count) 
            count = 1
        previous_char = chatacter
        i = i + 1
        
    return result + previous_char + str(count) 

print(run_length(str_in))