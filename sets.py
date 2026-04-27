sample = set()  #{}

print({'a', 'b', 'a'})
sample = {'a', 'b', 'a'}
print(sample)

# Sets are an unordered collection
# Sets removes duplicates and stores unique values

# print(dir(set()))

"""

['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

"""
sample.add(10)
print(sample)

# ordered collection (such as list, tuple, dict) supports indexing
# unordered collection doesnt support indexing


s1 = {1, 2, 3, 4}
s2 = {2, 4, 6, 8}

print(s1.difference(s2))
s1.difference_update(s2)
print(s1)



