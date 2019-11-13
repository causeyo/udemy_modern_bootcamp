"""
if file is not created, it will be created

modes:
r - read - default mode
w - write (previous content removed)
a - append (previous content not removed - seek doesn't work - always at the end)
r+ - read and write to file - based on cursor - working only with existing files

"""
# if we open file one more time with 'w' mode it will be overwritten

with open("poem.txt", "w") as file:
    file.write("I like to read\n")
    file.write("I like to skate\n")
    file.write("reading is good\n")
    file.write("but writing is great!")

with open("poem.txt", "a") as file:
    file.write("one more line at the end of file\n")

with open("poem.txt", "r+") as file:
    file.write("start writing from the beginning")
    file.seek(20)
    file.write("writing after cursor moving")
