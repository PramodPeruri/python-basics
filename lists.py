server_1 = "172.285.33.1"
server_2 = "172.25.20.1"

servers = ["172.285.33.1", "172.25.20.1", "172.25.20.8", True, 142 ] # This is a list
print(type(servers), servers[3] )  # using index to print particular value

# Slicing (we mention start_index:end_index) here end_index is not inculsive
simple_slice = servers[1:4]
#Step Size example 1 is default
step = servers[0:4:2] # Step size 1, 1+2
print(simple_slice)
print(step)

# negative indexing
simple_slicen = servers[-1] #gives last element in the list
print(simple_slicen)
print(len(servers)) # Length of the element

# List is a mutable datatype
# Muatble - once defined change at anytime Eg: List, dict
# Immutable - once defined can't be changed Eg: tuple, sets

print("before modify:", servers)
servers[-3] = 1234 # Inplace Operation
print("After modification:", servers)

print("List of Operations:", dir(servers)) # dir is used to get what kind of the operations can be done.

servers.append(False)
print(servers)

#Multi Indexing
# servers[-1][0]

# extend
servers.extend(["a", "b"]) # shows as seperate elements not combined like append
print(servers.index(True)) # gives the index number of the value
servers.insert(0, 12) # Inserts the objects
print(servers)

servers.remove(True) # removes the first occurence

servers.reverse() # Gives reverse of the data 
servers[::-1] # this is the reverse of the list, this also we can use.

servers.sort() #Sorts the data in the order, you will lose the original list once sort is done.

sorted(servers) #gives the new list in the ascending order

servers_1 = servers.copy()

"""
1. Reverse alist
2. sort vs sorted
3. Integer division vs floor division
4. shallow copy( inplace operation)
5. multi indexing
6. append vs extend
7. mutable vs immutable
8. dir()

"""

