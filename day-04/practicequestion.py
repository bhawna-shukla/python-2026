#WAP TO ASK USER TO ENTER  NAMES OF THEIR 3  FAVORITE MOVIE & store them in a list 
movies = []
mov = (input("Enter your favorite movie name: " ))
movies.append(mov)
mov = (input("enter the 2nd movie : "))
movies.append(mov)
mov = (input("enter  the 3rd movie : "))
movies.append(mov)
print(movies)
print("------------------")
#second way of code
color = []
color.append(input("enter 1 color :"))
color.append(input("enter 2 color :"))
color.append(input("enter 3 color :"))
print(color)
print("-----------------------")
#WAP TO CHECK IF A LIST  CONTAINS A PALINDROME OF  ELEMENT  
list = []
list.append(input("enter 1 no.:"))
list.append(input("enter 2 no.:"))
list.append(input("enter 2 no.:"))
print(list)

copy_list= list.copy()
copy_list.reverse()

if (copy_list== list):
    print("yes is a palindrome")
else:
    print("not a pallindrome ")
print("--------------------------")
#WAP TO COUNT THE NUMBER OF STUDENT WITH THE  GRADE "A" IN THE FOLLOWING TUPLE
grade = ("A" ,"B" ,"C" ,"A" , "A" , "C" , "D" , "A")
print(grade.count("A"))
print("-------------------------------")
#STORE THE ABOVE VALUES IN A LIST & SORT THEM
grade1= ["A" ,"B" ,"C" ,"A" , "A" , "C" , "D" , "A"]
grade1.sort()
print(grade1)
print("THANKYOU ")