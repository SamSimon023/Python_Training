#writing to a file

with open("sample.txt","w")as f:
    f.write("Hello, this is the 1st line.\n")
    f.write("This file was created using python.\n")

#reading from same file.

with open("sample.txt","r") as f:
    content = f.read()
    print(content)