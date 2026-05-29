#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.


info = {
    "name" : "Bhawna",
    "age" : 24,
    "city" : "lucknow",
    "marks" : 87
}
print(info)
print("--------------------")
print(info["name"])
print(info["city"])
print("------------------")
#Add the some kyes and value 
info["name"] = "Bhawna"
info["surname"] = "Shukla"
print(info)
print("------------------")
#null dictionary
null = {}
null ["name"] = "varsha"
print(null)