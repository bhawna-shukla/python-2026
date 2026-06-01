#python can be used   to perform  operation on a file (read & write)
# types of file
# text file
# binary file

f = open("C:\\Users\\Bhawn\\OneDrive\\Desktop\\python-2026\\day-09\\demo.txt","w")

# data = f.read()
data = f.write(" \nafter  learn mern stack  ")
# print(data)
# print(type(data))
f.close()

#reading file 
#1.read()
# 2 readline()
# "r+"   isme read or write dono hoga 


#writing the file
#1 write "w"  .........truncate the file means previous wala delete ho jayega or new create hoga 
f = open("C:\\Users\\Bhawn\\OneDrive\\Desktop\\python-2026\\day-09\\sample.txt","a")
data = f.write("this is my second file")

f.close()

#2. "a" write ke baad mai jo bhi add karoge woh add ho jayega
#"w+" isme over rite hoga like 
