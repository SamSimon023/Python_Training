#program to read and print the contents of notes.txt line by line.

with open("notes.txt","r") as f:
    content=f.read()
    print(content)

f.close()
