t = () 
t1 = tuple()

sample = ("172.285.33.1", "172.25.20.1", "172.25.20.8", True, 142)
print(type(sample), sample)

# tuple is immutable
print(sample[0])
# sample[0] = 12
print(sample[0:2])
print(sample[-1])

envs_list = ["DEV", "QA", "PREPOD", "PROD"]

# print(dir(tuple))

"""
Count and index

"""

sample = (1,2,3,4,5,4)
print(sample.count(5), sample.count(12))
print(sample.index(5))

# type casting: Data Type conversion
sample = ("172.285.33.1", "172.25.20.1", "172.25.20.8", True, 142)
sample_1 = list(sample)
print(type(sample_1))
sample_t = tuple(sample_1)
print(type(sample_t))


