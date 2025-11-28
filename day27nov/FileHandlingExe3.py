#appends a new line to an existing file notes.txt that says:
#"This is an appended line."

with open("notes.txt","a")as f:
    f.write("\nThis is an appended line.")

with open("notes.txt","r") as f:
    content=f.read()
    print(content)

f.close()