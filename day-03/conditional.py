#WA programe to intput the traffic light color and print the action to be taken
color = input("enter the any one color of traffic light color :")
if color == "red":
    print("stop")
elif color == "yellow":
    print("ready")
elif color == "green":
    print("go")

else:    
    print("invalid color")

print("---------------------------------")
#eligible for voting or not
age = int(input("enter your age :"))
if age >= 18:
    print("you are eligible for voting")
else: 
    print("you are not eligible for voting")

print("---------------------------------")
#Write a program to print grades according to marks.
marks = int(input("enter your marks :"))
if marks>=90:
    grade = "A"
elif (marks>=80 and marks<90):
    grade = "B"
elif (marks>=70 and marks<80):
    grade = "C"
elif (marks>=60 and marks<70):
    grade ="D"
print("your grade is :",grade)
print("---------------------------------")

#nesting of if statement
drive_age =int(input("enter your age:"))
if drive_age >18:
    if drive_age >=90:
        print("you are too old to drive")
    else:
        print("yes you can drive")
else:
    print("you are not eligible to drive")