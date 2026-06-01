#resursive function    same loop ki tarah ki work karta hai 

#Recursion in Python is a programming technique where a function calls itself to solve a problem by breaking it down into smaller, similar subproblems.

# A recursive function usually has:
# Base case – the condition that stops the recursion.
# Recursive case – where the function calls itself.


def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5)
print("-----------------------------")
#factorial

def cal_fact(n):
    if(n == 1 or n == 0):
        return 1
    return cal_fact(n-1) *n

print(cal_fact(5))

#natural number with sum

ans = int(input("enter the number:"))
def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n 

print(cal_sum(ans))

#WA recursive  function  to print  all element  in a list hint: use list & index  as parameter 
fruits = ["mango","orange","litchi","lemon"]

def cal_list(list,idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    cal_list(list,idx +1)


cal_list(fruits)
