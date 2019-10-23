### THE MOST BASIC EXAMPLE ###
try:
    notdefined
except:
    print("some problem exists!!!")
print("print executed at the end")


### BUT WE SHOULD BE MORE SPECIFIC WITH EXCEPTION DEFINITIONS ###

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

d = {"name": "Phil"}
get(d, "name") # Phil
print(get(d, "last")) # None
