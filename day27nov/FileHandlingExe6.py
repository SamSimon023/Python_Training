#copy the contents of one file ( source.txt ) to another file ( backup.txt ).

with open("source.txt","w+") as f:
    content="This is content from original file"
    f.write(content)
f.close()

with open("backup.txt","w") as f:
    f.write(content)
    f.write("\n\tCopied")

f.close()
print("File copied successfully")