#WAF TO PRINT THE LENGHT OF A LIST (LIST ID THE PARAMETER)

cities = ["delhi","punjab","mumbai","goa","chennai", "gurgoan"]
heroes = ["ironman","thor","spoderman","krish","shaktiman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

#WPF to print the element of a list in a single line (list the parameter )
def print_el(list):
    for i in list:
        print(i,end=" ")
    
print_el(cities)
print()

#WAP to find the factorial of n ( n is parameter)

def cal_fact(n):
    fact = 1
    for val in range(1, n+1):
        fact *= val
    print(fact)

cal_fact(6) 

#WAF to convert  USD to INR

def convert(USD):
    inr = USD * 94.84
    print(USD,"USD=",inr , "inr")

convert(7)


#HOME WORK QS 


def cal_math(num):
    if(num%2==0):
        print(num,"is a even number")
    else:
        print(num,"is a odd number")
        
num=cal_math(3)











    