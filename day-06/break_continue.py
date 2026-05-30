# the break statement we can stop the loop even if the while condition is true
i =1 
while i<=5:
    print(i)
    if( i==2):
        break
    i +=1
print("--------------------------------")
t = (1,4,9,16,25,36,49,64,81,100)
f = 16
d = 0
while d < len(t):
    if(t[d] == f):
        print("found it :",d)
        break     #stop
    else:
        print("finding ........")
    d += 1
print("------------------")
j = 1 
while j<=5:
    if(j==2):
        j+=1
        continue
    print(j)
    j+=1   #skip


