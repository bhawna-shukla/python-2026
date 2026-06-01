#function definition
# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.
#In Python, a function is defined using the def keyword, followed by a function name and parentheses:



def cal_sum(a,b): #parameters
    sum = a+b 
    print(sum)
    return sum

cal_sum(5,6)   #function call   ;   arguments

cal_sum(678,89)
#simple cod

def cal_sum(a,b):
    return a + b

sum = cal_sum(1,2)
print(sum)


#print hello 
def print_hello():
    print("helllo")

print_hello()
#average of three number 
def avg_num(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg
 
avg_num(2,4,6)
print("---------------------")

