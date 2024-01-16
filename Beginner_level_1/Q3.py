"""
3. Write a Python program to input marks for five subjects Physics,Chemistry, Biology, Mathematics, and Computer. 
Calculate thepercentage and grade according to the following:
- Percentage >= 90% : Grade A
- Percentage >= 80% : Grade B
- Percentage >= 70% : Grade C
- Percentage >= 60% : Grade D
- Percentage >= 40% : Grade E
- Percentage < 40% : Grade F
"""
Physics_marks = float(input("Enter the marks out of 100 for Physics : "))
Chemistry_marks = float(input("Enter the marks out of 100 for Chemistry : "))
Biology_marks = float(input("Enter the marks out of 100 for Biology : "))
Mathematics_marks = float(input("Enter the marks out of 100 for Mathematics : "))
Computer_marks = float(input("Enter the marks out of 100 for Computer : "))

total = Physics_marks + Chemistry_marks + Biology_marks + Mathematics_marks + Computer_marks 
Percentage = round((total/500.0) * 100 , 2)
if Percentage >= 90:
    print(f"your Percentage is {Percentage} and you have achieved Grade A ")
elif Percentage >= 80:
    print(f"your Percentage is {Percentage} and you have achieved Grade B ")
elif Percentage >= 70:
    print(f"your Percentage is {Percentage} and you have achieved Grade C ")
elif Percentage >= 60:
    print(f"your Percentage is {Percentage} and you have achieved Grade D ")
elif Percentage >= 40:
    print(f"your Percentage is {Percentage} and you have achieved Grade E ")
elif Percentage < 40:
    print(f"your Percentage is {Percentage} and you have achieved Grade F ")
