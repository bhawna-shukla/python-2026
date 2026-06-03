#Create a student  class that takes  name & marks of 3 subject  as argunment in constructor then  create  a method  to print the average 

class student():
      def __init__(self,name,marks):
            self.name = name
            self.marks = marks

      def get_avg(self):
            sum = 0 
            for val in self.marks:
                  sum += val
            print("hii:",self.name,"your avg score is :" ,sum/3)


s1 = student("varsha",[90,80,99])
s1.get_avg()
