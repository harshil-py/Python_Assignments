"""
12. Create a login page backend to ask users to enter the username
and password. Make sure to ask for a Re-Type Password and if the
password is incorrect give a chance to enter it again but it should
not be more than 3 times.
"""
username = "group_admin"
password = "abc123"
count = 0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter Password: ')
    re_type_password = input('Re-Type the password: ')
    if password and re_type_password == "abc123" and username == "group_admin":
        print("Access granted")
        break
    else:
        print("Access denied. Try again.")
        count += 1

