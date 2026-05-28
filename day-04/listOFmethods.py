#add on element of the end 
list = [2,3,4,5,7,8,4,6,9]
list.append(50)
print(list)
print("----------------------")
#sort in ascending order
list.sort()
print(list)
print("-------------------")
#sorts in decending order
list.sort(reverse=True)
print(list) 
print("----------------------")
list.reverse()
print(list)
print("------------------------")
#insert element at index 
lists = ['q','e','r','e','t']
lists.insert(3,'s')
print(lists)
print("--------------------")
#removes first occurence of element 
lists.remove('e')
print(lists)
print("-------------------------")
#remove element  at index
lists.pop(2)
print(lists)
