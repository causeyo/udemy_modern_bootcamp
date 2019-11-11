# WITHOUT A GENERATOR....
# To generate first 1,000,000 fib numbers, it has to store all of them in a list
def fib_list(max):
     nums = []
     a, b = 0, 1
     while len(nums) < max:
         nums.append(b)
         a, b = b, a+b
     return nums

# print(fib_list(50000))


# USING A GENERATOR...
# To generate first 1,000,000 fib numbers,no list needed!
def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count+=1


# for n in fib_gen(100000):
#     print(n)


# we can check linux memory usage on live preview with command 'watch -n 1 free -m'