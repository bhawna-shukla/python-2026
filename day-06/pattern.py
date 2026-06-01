num = int(input("enter the number : "))

for i in range(0,num+1):
    for j in range(i+1):
        print("*",end=" ")
    print()

print("-----------------------")


#pattern 
n = int(input("enter the number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print() 