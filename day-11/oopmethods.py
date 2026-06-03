#Mehods are  function  that belong  to object 
#creating methods
class student:

     def __init__(self,name,marks,batch):        #object
         self.name = name
         self.marks = marks
         self.batch = batch

     def welcome(self):   #method
          print("welcome student:",self.name)
         
     def get_marks(self):
          return self.marks
        

s1 = student("bhawna",90,"bca")
s1.welcome()
print(s1.get_marks())

#question 


          