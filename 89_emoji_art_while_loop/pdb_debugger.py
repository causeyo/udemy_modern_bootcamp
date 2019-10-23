# silent errors - something went wrong but there is no error thrown
import pdb


first = "First"
second = "second"
pdb.set_trace()
result = first + second
third = "third"
result += third
print(result)

# to set breakpoint to start investigation
# import pdb
# pdb.set_trace()
#
# or oneliner
#
# import pdb; pdb.set_trace()


# Common PDB commands:
# l (list)
# n (next line)
# p (print) -> e.g. if our variables are the same with commands like 'c' -> you can use 'p c'
# c (continue - finishes debugging)