def nums():
    for num in range(1,10):
        yield num

g = nums()
print(next(g))
print(next(g))

# equivalent is generator expression

g2 = (num for num in range(1,10))

print(next(g2))



import time
#
# SUMMING 10,000,000 Digits With Generator Expression
gen_start_time = time.time()  # save start time
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time  # end time - start time

# SUMMING 10,000,000 Digits With List Comprehension
list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time
#
# print("sum(n for n in range(10000000)) took: {}".format(gen_time))
# print("sum([n for n in range(10000000)]) took: {}".format(list_time))