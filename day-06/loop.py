#while loop
count = 1
while count<=10 :
    print("hello")
    count+=1
print("loop end")
print("-------------------")
#print 1 to 10 number 
i = 1
while i<=10 :
    print(i)
    i+=1
print("end")
print("----------------------")
#reverse counting 1 to 20 in while loop
num = 20
while num>=1 :
    print(num)
    num-=1
print("end")

#SOME [RACTICE QUESTIONS ]
#PRINT A NUMBER  FROM 1 TO 100
x = 1
while x<=100 :
    print(x)
    x += 1
print("number  1 to 100")
print("------------------------")
y = 100
while y>=1 :
    print(y)
    y -= 1
print("reverse  number 100 to 1")
print("----------------------")
#PRINT THE MULTIPLICATION TABLE OF A NUMBER N 
n = int(input("Enrer the number :"))
tab = 1
while tab<=10 : 
    print(n*tab)
    tab += 1
print("here is your table of :",n)
print("----------------------")
#Print the element of the following list using a loop
lis = [1,4,9,16,25,36,49,64,81,100]
idx = 0 
while idx < len(lis) :
    print(lis[idx])    #num[0] num[1] num[2]
    idx +=1
print("----345--------------")
#SEARCH FOR  A NUMBER X  IN THIS TUPLE USING LOOP
t = (1,4,9,16,25,36,49,64,81,100)
f = 81
d = 0
while d < len(t):
    if(t[d] == f):
        print("found it :",d)
    else:
        print("finding ........")
    d += 1
print("------------------------")