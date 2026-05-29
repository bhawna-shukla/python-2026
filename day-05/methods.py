#return  all keys
student ={
    "name" : "rahul",
    "subject" : {
    "math" : 78,
    "phy" : 58,
    "chem" : 89,
    "eng" : 99
    }
}
print(student)
print("mark is: ",student["subject"]["math"])
#print only key 
print(student.keys())
#return all values
print(student.values())
print("-------------------")
print("covertion of list and tuple")

print(list(student.keys ()))
print("------------------")
print(tuple(student.keys()))


print("-------------------")
#return all (key,value )pairs as tuple
print(list(student.items()))
print("---------------")
pair = list(student.items())
print(pair[0])
print("------------")
#return the key according to value
#print(student(["name "])     -------ERROR------- iske agge  excute nhi hoga jab tak error khatam na ho jaye  
print(student.get("name2")) # no error 
#isme error nhi deta hai age excute  kar deta hai 
print("-----------------------")
#insert the specified item to the dictionary
student.update({"city" : "gujrat"})
print(student)
print("----------")
#similar second way
new_dic = {"mobile no." : 8939726 , "landmark" : "shiv mandir"}
student.update(new_dic)
print(student)