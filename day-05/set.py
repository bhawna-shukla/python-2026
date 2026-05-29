#Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.

my_set = {1,3,2,3,3,"apple" , "mango",5}
print(my_set)
print(len(my_set))
print(type(my_set))

print("--------------------")
collection = {}        #no empty set
print(type(collection))
print("--------------------")
new_set = set()     #this is empty set
print(type(new_set))