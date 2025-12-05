#program to create a file named notes.txt and write 5 lines of text into it.

with open("notes.txt","w") as f:
    f.write("This is line 1 \nThen comes line 2\nThen there is a 3rd line\nWhich is followed by the second last line\nand finally the 5th and final line.")

f.close()