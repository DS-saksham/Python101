# Lists: oredered , mutable and allows us to dupicate elements
mylist = ["Apple", "Cherry", "Banana"]
print(mylist)
print(mylist[1])

if "Cherry" in mylist:
    print("Cherry is Present")
else:
    print("Cherry is Not Present")


print(mylist[::-1]) # Reversing the List 

list_org = [1,2,3,4,5]
list_copy = list_org
list_copy1 = list(list_org)

# List Comprehensions
a = [1,3,4,4,34,5]
b = [i+i for i in a ]
print(a)
print(b)
