# try:
# except:
# else:
# finally:

try:
    num = int(input("please provide a number: "))
except:
    print("thats not a number!")

# we can add more options with ELSE statement -> if except doesn't run, else will be triggered

try:
    num = int(input("please provide a number: "))
except:
    print("thats not a number!")
else:
    print("thats ELSE statement, will be run only when except is not triggered")

# we can add FINALLY statement -> will be run, no matter what

try:
    num = int(input("please provide a number: "))
except:
    print("thats not a number!")
else:
    print("thats ELSE statement, will be run only when except is not triggered")
finally:
    print("this will be run no matter what")

# and now we can make while loop which will be running till int will be provided for input
while True:
    try:
        num = int(input("please provide a number: "))
    except:
        print("thats not a number!")
    else:
        print("thats ELSE statement, try executed successfully")
        break
    finally:
        print("this will be run no matter what, even after break")
print("Number is provided, break and finally executed, we can move on!")