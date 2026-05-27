#Write a program to check whether a number is even or odd.
num = int(input("enter a number : "))
if num % 2==0:
    print("the number is even")
elif num % 2 !=0:
    print("the number is odd")



print("---------------------------------")
# Positive, Negative, or Zero
a  = int(input("enter the number : "))
if a > 0:
    print("this ia a number of positive :",a)
elif a < 0:
    print("this is a number of negative :",a)
else:
    print("this is a number of zero :",a)
print("------------------------------" )

# Largest of Two Numbers
num1 = int(input("enter first number :"))
num2 = int(input("enter second number "))
if num1 > num2 :
    print("the lagrgest number is  :",num1)
elif num1<num2 :
    print("the largest  number is",num2)
else:    
    print("both numbers are equal")
print("----------------------------------- ")
#Divisible by 5
div = int(input("enter a number divisible by 5 "))
if div % 5 ==0:
    print("the number is divisible by 5")
else:
    print("the number is not divisible by 5")
print("----------------------------------")

#6. Pass or Fail
marks = int(input("enter your marks : "))
if marks>=35:
    print("congratulations you have passed the exam")
else: 
    print("sorry you have failed the exam")
print("-------------------------------------   ")
#7. Leap Year
yr = int(input("enter a year : " ))
if yr %4 ==0 :
    print("the year is leap year")
else:
    print("the year is not a leap year")
    print("-----------------------------------")
    # Greatest of Three Numbers
gr = int(input("enter first number - "))
gr1 = int(input("enter second number -"))
gr2 = int(input("enter third number - "))
if gr>=gr1 and  gr>=gr2:
    print("the greatest number is :",gr)
elif gr1>=gr and gr1>=gr2:
    print("the greatest number is :",gr1)
else:
    print("the greatest number is :",gr2)
print("-----------------------------------")
# Vowel or Consonant
ch = input("enter a charcter : ")
if ch in ("a" ,"e", "i", "o", "u", "A", "E", "I", "O", "U"):
    print("the character is vowel")
else:
    print("the character is consonant")
    print("-----------------------------------")
#percentage 
per = int(input("enter your marks : "))
percentage = (per/500)*100
print("your percentage is : ",percentage)
print("-----------------------------------")

#11. Multiple of 3 and 7
mul = int(input("enter the number :"))
if mul %3 ==0 and  mul %7 ==0:
    print("the number is multiple of 3 and 7")
else:
    print("the number is not a multiple of 3 and 7")