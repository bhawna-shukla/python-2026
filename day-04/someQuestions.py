#Find sum of all elements in a list
nums = []
nums.append(int(input("enter the number :")))
nums.append(int(input("enter the number :")))
nums.append(int(input("enter the number :")))
nums.append(int(input("enter the number :")))
nums.append(int(input("enter the number :")))
nums.append(int(input("enter the number :")))
print("you enter this number : " , nums)
total  = sum(nums)
print("sum of the total  number : ", total)
print("----------------------------------")
#Find largest number in a list
num = []
num.append(int(input("enter the number :")))
num.append(int(input("enter the number :")))
num.append(int(input("enter the number :")))
num.append(int(input("enter the number :")))
num.append(int(input("enter the number :")))
num.append(int(input("enter the number :")))
print("your number is :",num)
large=max(num)
print("The Largest number is : ", large)
print("-----------------------")
#Find minimum element in tuple
small = min(num)
print("Then minimum number is :" , small)
print("----------------------")
#Convert list into tuple
list = [1,3,5,7,2]
my_tuple = tuple(list)
print(my_tuple)
print("---------------------------")
#Remove duplicate elements from a list
num1= [1, 2, 2, 3, 4, 4, 5]
unique = set(num1)
print(unique)
print("----------------------------")
#Swap first and last element of a list
x = [20,40,30,10,50]
x[0],x[-1] = x[-1],x[0]
print(x)


