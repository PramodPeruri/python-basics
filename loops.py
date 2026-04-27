# for, while
# continue, break

# value = 0

# while value < 10:
#     print(value)
#     value = value + 1

# value = 0

# while value < 10:
#     if value == 5:
#        break
#     print(value)
#     value = value + 1


# value = 0

# while value < 10:
#     if value == 5:
#         value = value + 1 # incrementing is very important otherwise it will be stuck in infinte loop
#         continue
#     print(value)
#     value = value + 1


sample = ["server1", "server2", "server3", "server4"]

# idx = 0

# while idx < len(sample):
#     print(sample[idx])
#     idx += 1 #idx = idx + 1


# in -> membership operator (checks whether that element is present or not)

# print(1 in sample) # gets false as output
# print("server1" in sample) # get true as output

# idx ->  iterator
# sample -> iterable

# for idx in sample:
#     print(idx)

# access elements inside a list with index using for loop
# range, enumerate

# range is a function, we need to specify start and end index and step

# print(list(range(5)))

# for idx in range(len(sample)):
#     print(sample[idx])

print(enumerate(sample))
for val in enumerate(sample):
    print(val)

# # Tuple unpacking
# a,b = (1,2)
# print(a, b) 

# while loop can be used when we know when to end
# for loop can be when we don't know when to end