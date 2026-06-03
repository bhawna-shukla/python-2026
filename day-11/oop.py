#oop to map  with real world scenerio , we started using object in code 
# this called object oriented programming (OOP)
# class is a blueprint for creating objects
#object is an instance of a class



# class student:
#     name = "tom"

# s1 = student()
# print(s1.name)

#_int_ is a constructor method that is called when an object is created
class student:

     def __init__(self,name,marks,batch):
         self.name = name
         self.marks = marks
         self.batch = batch
         
        

s1 = student("bhawna",90,"BCA")
s2 = student("Ram",90,"BBA")
print("id:",s1.name,s1.marks,s1.batch)
print("id:",s2.name,s2.marks,s2.batch)

