print("\n{0} first example - file method read() {0}".format(10*"#"))

f = open(file='schtory.txt')
data = f.read()
print("\nfirst reading data: {}".format(data))

data1 = f.read()
print("\nsecond reading data: {}".format(data1))
# second reading is empty because cursor stopped at the end of the file

f.seek(0)
data2 = f.read()
print("\nthird reading data: {}".format(data2))
# # with f.seek(0) cursor was moved to beginning so file can be read one more time

print("\n{0} second example - file method readline() {0}\n".format(10*"#"))

# readline method is reading one line at the time
f.seek(0)
line1 = f.readline()
print("first read line: {}".format(line1))

line2 = f.readline()
print("second read line: {}".format(line2))

line3 = f.readline()
print("third read line: {}".format(line3))

line4 = f.readline()
print("fourth read line is empty because file ends: {}".format(line4))

print("\n{0} third example - file method readlines() {0}\n".format(10*"#"))

# readlines method returns list of all lines
f.seek(0)
lines = f.readlines()
print("list of lines: {}".format(lines))

# after finished work with file, it should be closed
print("before file closing f.closed is {}".format(f.closed))

print("then f.close() is executed")
f.close()
print("after file closing f.closed is {}".format(f.closed))