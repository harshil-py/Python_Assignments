"""
8. You need to write a function that accepts an encoded string as a
parameter.
This string will contain a first name, last name, and an id.
Values in the string can be separated by any number of zeros. The
id is a numeric value but will contain no zeros. The function should
parse the string and return a Python dictionary that contains the
first name, last name, and id values.
For example:
Input : “Robert000Smith000123”
Output:
{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }
"""
in_str = "Robert000Smith000123"
def encoded_string(in_str):

    #x=input("Enter string:")

    p=in_str[::-1]

    a=""
    new_str = ""
    for i in range(len(p)):

        if p[i]=="0":
            a=a+p[0:i]
            str_id=a[::-1]
            p_str = new_str+p[i::]
            new_str = p_str[::-1]
            break
    
    b=""
    temp_str=""
    for i in range(len(new_str)):

        if new_str[i]=="0":
            first_name=b+new_str[0:i]
            temp_str = temp_str + new_str[i::]
            break
    
    for i in range(len(temp_str)):
        if temp_str[i]=="0":
            temp_str = temp_str.replace(temp_str[i]," ")

    last_name = temp_str.strip()
    
    
    return {"first_name": first_name, "last_name": last_name, "id": str_id}

print(encoded_string(in_str))
    