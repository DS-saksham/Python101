# Dictioanary: They are Unordered , Mutables and are in the form of Key Value Pairs

mydict = {"Name" : "Saksham", "Age" : 20, "Language" : "Nepal"}
print(mydict)

mydict2 = dict(name="Harry", age =27 , city ="Boston")
print(mydict2)

value = mydict["Name"]
print(value)

#Adding the Elements
mydict["Email"] = "Saksham44humagain@gmail.com"

#Removing the Elements
del mydict["Name"]

#Exception Handeling in Python
try:
    print(mydict["Age"])
except:
    print("Error")


#Lopping
for key in mydict2:
    print(key)

for key, value in mydict2.items():
    print(key,value)
