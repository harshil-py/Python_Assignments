"""
1.Read the doc.txt file using Python File handling concept and
return only the even length string from the file. Consider the
content of doc.txt as given below:
Hello I am a file.
Where you need to return the data string which is of even length.
Make sure you return the content in The same link as it is present.
"""

with open("doc.txt", "r") as f:
    all_lines = f.readlines()
    for i in all_lines:
        if len(i) % 2 == 0:
            print(i)