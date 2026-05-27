#1. Simple Interest 
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))
si = (p * r * t) / 100
print("The simple interest is:", si)
if si>=1000:
    print("high interest")
else:
    print("low interest")
print("-----------------------------------")    

#2. Area of Circle
pi = 3.14
r = float(input("Enter the radius of the circle: "))
area = pi * r * r
print("The area of the circle is:", area)
if area > 100:
    print("Large Circle")
else:
    print("Small Circle")
print("-----------------------------------")
#3. BMI Calculator
#body mass index
w = float(input("Enter your weight in kg: "))
h = float(input("Enter your height in meters: "))
bmi = w / (h * h)
print("Your BMI is:", bmi)
if bmi >= 30:
    print("over weight")
else:
    print("Normal weight")
print("------------------------------------")
#4 Speed Calculator
distance = float(input("Enter distance:"))
time = float(input("Enter time: "))

speed = distance / time

print("Speed =", speed)

if speed > 60:
    print("Fast Speed")
else:
    print("Normal Speed")
print("-----------------------------------")
#5. Electricity Bill Calculator
u = int(input("Enter the number of units consumed: "))
bill = u * 5
print("Your electricity bill is:", bill)
if bill > 500:
    print("High Bill")
else:
    print("Low Bill")
    print("-----------------------------------")
#6 Profit or Loss
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

profit = sp - cp

if profit > 0:
    print("Profit =", profit)
else:
    print("Loss =", abs(profit))
print("-----------------------------------")
# Temperature Converte
c = float(input("Enter temperature in Celsius: "))

fah = (9/5) * c+ 32

print("Temperature in Fahrenheit =", fah)

if fah> 100:
    print("Very Hot")
else:
    print("Normal Temperature")
print("-----------------------------------")
# Discount Calculator
p = float(input("Enter the price: "))
d = float(input("Enter the discount percentage: "))
discount_amount = d * p /100
if discount_amount > 50:
    print("High Discount")
else:
    print("Low Discount")
print("-----------------------------------")
# Salary Bonus Calculator
salary = float(input("Enter your salary: "))
bonus = salary * 0.10
print("Your bonus is:", bonus)
if bonus > 5000:
    print("High Bonus")
else:
    print("Low Bonus")
print("-----------------------------------")
