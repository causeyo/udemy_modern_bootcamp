# first option
file = open("schtory.txt")
file.read()
print("before file closing file.closed is {}".format(file.closed))
file.close()
print("after file closing file.closed is {}".format(file.closed))

# second option
with open("schtory.txt") as file:
    file.read()
    print("inside with statement file.closed status is {}".format(file.closed))
print("outside with statement file.closed status is {}".format(file.closed))