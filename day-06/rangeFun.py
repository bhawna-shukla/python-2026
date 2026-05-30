#The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.

#This set of numbers has its own data type called range.
#The range() function can be called with 1, 2, or 3 arguments, using this syntax:



for n in range(5):   #start with by  0
     print(n)



for m in range(2,20,1):     #start,stop,step
     print(m)


print("----------------------------")
for i in range(1,20):
     print(i)

#Qsprint tje number 1 to 100
for num in range(1,101):
     print(num)

print("  -------------------------")


#Qs Print the number 100 to 1
for num1 in range(101,0,-1):
     print(num1)


print("---------------------------------------")
#Qs print tht multiplication  table of a number mul
mul = int(input("enter the number :"))
for num2 in range(1,11):
     print(mul*num2)


print("---------------------------------")
for j in range(10):
     pass

print("this  is empty")

#practice qs 
nan = 5

sum = 0
for k in range(1, nan+1):
     sum += k

print("total number :", sum)

print("------------------")
fa = 5
fact  = 1
for val2 in range (1, fa+1):
        fact *=val2

print(fact)
 
           


