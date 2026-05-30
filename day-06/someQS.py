#Write a program to print all even numbers from 1 to 20 using a while loop.
i=2
while i <=20:
    if i%2==0 :
        print(i)
    i +=1
#Write a program to find the sum of numbers from 1 to N using a while loop.
n = int(input("Enter a number: "))
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i += 1

print("Sum =", sum)
print("-------------------")
#Write a program to count the number of digits in a given number using a while loop.
num1 = int(input("Enter a number: "))

count = 0

while num1 > 0:
    num1 = num1 // 10
    count += 1

print("Number of digits =", count)
print("------------------------")
#Write a program to print the Fibonacci series up to N terms using a while loop.
val= int(input("Enter the number of terms: "))

a = 0
b = 1
add = 0

while add < val:
    print(a,end=" ")
    
    c = a + b
    a = b
    b = c
add += 1
print("----------------------")
    #Write a program to find the factorial of a number using a while loop.
num2 = int(input("Enter a number: "))

fact = 1
h = 1

while h <= num2:
    fact = fact * h
    h += 1

print("Factorial =", fact)