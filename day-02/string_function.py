#returns true if string ends with substr (endswith())
str = "apna school"
print(str.endswith("hool"))
print(str.endswith("hoop"))

print("--------------------------")
#capitalize() capitalize  1 char
str1 = str.capitalize()
print(str1)

print("--------------------------")
#replace(old.new) replaces all occurrences of old with new
str3 = str.replace("a" ,"o")
print(str3)

print("--------------------------")
#find(sub) returns the index of first occurrence of sub in string. If sub is not found, it returns -1
str4 = str.find("n")
print(str4)

print("--------------------------")
#count(sub) returns the number of occurrences of sub in string
str5 = str.count("o")
print(str5) 








#WAP to the occurence  of $ in a string 
val = " $1000 is the price of this product. I have $500 in my wallet."
val1 = val.count("$")
print(val1)

#WAP to input user's  first name & print its  lenght
name = input ("Enter your name :")
name1 = len(name)
print(name1)
print("-------------")
#Q7. Write a program to reverse a string.
text = "Madam"
reverse_text = text[::-1]
print(reverse_text)