d = {}
d_1 = dict() # Key value pair


# Dictionaries are key value pair also known as hash map 
sample = {'a': 1, 'b': 2}
print(sample['a'], sample.get('b'))

# Dictionaries are mutable data type 
sample['a'] = 10
print(sample)

# Keys in dictonaries once defined can't be changed
# Hence they should be of immutable datatype eg tuple, string

sample = {("a", "b"): 1, 'b' : 2}
print(sample)

# print(dir(dict))

"""
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

"""

print(sample.keys(), sample.values())

sample_list = [(('a', 'b'), 1), ('b', 2)]
print(type(sample_list))

sample_dict = dict(sample_list)
print(sample_dict)
print(type(sample_dict))