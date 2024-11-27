# It is used to generate a new list by applying an expression to each item in an iterable(like a list,tubles) \
# WHile optionaly including the filtering condition
list = [1,2,3,4]
print(list)

# List Comprehension
new_list = [i*3 for i in list if i%2 == 0]
print(new_list)

#Finding the Square of number
squares = [x**2 for x in range(10)]
print(f"The list of square numbers is {squares}")

# For Strings
uppercase = [char.upper() for char in "Saksham"]
print(uppercase)


#Nested Lopps in List Comprehension
pairs = [(x,y) for x in range(4) for y in range(2)]
print(pairs)

# Advamced USe Cases 
#1. Flatten a Nested List
nested = [[1,2],[3,5],[3,1]]
flat = [item for sublist in nested for item in sublist ] # The first loop is outerlopp and the next is the inner
print(flat)
 
 # It is equivalent to::
 '''
 flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)
 '''

 #Conditiona;l Transformation
 results  = [x if x%2 == 0 else -x for x in range(10)]