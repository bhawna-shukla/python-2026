print("1. Arithmetic operators")
print('------------------') 
a = 2
b = 4
print("add the sum :" , a + b)  # Addition
print("subtract the difference :" , a - b)  # Subtraction
print("multiply the product :" , a * b)  # Multiplication

val1 = 10
val2 = 30
print("divide the quotient :" , val1 / val2 )  # Division
print("floor divide the quotient :" , val1 // val2)  # Floor Division
print("find the remainder :" , val1 % val2)  # Modulus
print("find the exponent :" , val1 ** 3)  # Exponentiation

print("")
print("2. Rational/ Comparison operators")
print('------------------')
print("")
x= 5
y= 6 
print("x is equal to y:", x == y)
print ("x is not equal to y:", x != y)
print("x is greater than y:", x > y)
print("x is less than y:", x < y)
print("x is greater than or equal to y:", x >= y)
print("x is less than or equal to y:", x <= y)
print("")
print("3. Assignment operators")
print('------------------')

num = 6
num += 5  # num = num + 5
print("num += 5:", num)
num -= 3  # num = num - 3
print("num -= 3:", num)
num *= 5  # num = num * 5
print("num *= 5:", num)
num /= 5  # num = num / 5
print("num /= 5:", num)
num //= 5  # num = num // 5
print("num //= 5:", num)
num %= 5  # num = num % 5
print("num %= 5:", num)
num **= 5  # num = num ** 5
print("num **= 5:", num) 
print("")
print("4. Logical operators")
print('------------------')
bool1 = True
bool2 = False
print("logical AND:", bool1 and bool2)  # Logical AND
print("logical OR:", bool1 or bool2)  # Logical OR
print("logical NOT:", not bool1)  # Logical NOT




print("")
print("----------------------------")
print("5. Membership operators")

numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # Check if 3 is in the list
print(6 not in numbers)  # Check if 6 is not in the list


print("")
print("----------------------------")

print("type conversion")
num1= 10
num2 =12.5
sum = num1 + num2
print ("the sum of num1 and num2 is:", sum)
print("")
print("----------------------------")
print("type casting ")
num3 = 15
num4 = 20.5
num3 = float(num3)  # Convert num3 to float
num4 = int(num4)  # Convert num4 to int
print("num3 after type casting to float:", num3)
print("num4 after type casting to int:", num4)
