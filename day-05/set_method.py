#ADD  add an element
my_set = set()
my_set.add(2)
my_set.add(3)
my_set.add(2)           #dublicvate element not allowed 
my_set.add("joker")
my_set.add("water")
print(my_set)
print("--------------------")

#REMOVE  remove an element
my_set.remove(3)
print(my_set)

print("------------------")
#CLEAR empties the set 
# my_set.clear()
# print(my_set)
# print(len(my_set))
print("--------------------")
#POP removes a random value
print(my_set.pop())
print(my_set.pop())
#union combine both set values & return new 
print("---------------------")
set1 = {1,2,3,4}
set2 = {1,4,2,4,5,6,}
print(set1.union(set2))
#intersection  combine common values & return new
print(set1.intersection(set2))


#SOME PRACTICE QUESTION 
dic = {
    "table": ["a piece of furniture", " list of fact & fiqure"],
    "cat" : "a small animal"
}
print(dic)
print("---------------------")
# 2  Q
subject = {"python","java","c++","python","javascript" ,"java","c++","python","java", "c"}
print(subject)
print(len(subject))
#   3Q
marks={}
x=int(input("Enter marks of phy "))
marks.update({"phy": x})
x=int(input("Enter marks of math "))
marks.update({"math": x})
x=int(input("Enter marks of chem "))
marks.update({"chem": x})
print(marks)
print("------------------")
value = {
    ("float" , 9.0),
    ("int" , 9)
}
print(value)
