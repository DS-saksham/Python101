# Sets are the collection data types that is unordered
# and mutable but we can not have the duplicates here
myset = {2,4,5,67,8,2,8,7}
print(myset)
myset_2 = set("Hello World!") # Here the data are not in the right order
print(myset_2)
myset.add(69)
print(myset)

if 'H' in myset_2:
    print("Yes")

# We can do the union, intersection , difference and symmetric difference of the different sets

# Disjoint sets :: The sets that have no any any common elements in 2 sets