#List 
#A list in Python is a built-in data structure used to store multiple items in a single variable
#It is ordered, mutable (changeable), and allows duplicate values.

#chainging list
# fruits = ["apple","banana"]
# fruits[0] = "mango"
# print(fruits)



#LIST METHODS
#append()
# fruits = ["apple","banana"]
# fruits.append("mango") #adds an element to the end of the list
# print(fruits)


#extend()
# fruits = ["apple","banana"]
# fruits1 = ["mango","perry"]
# fruits.extend(fruits1) #add multiple elements from another iterable
# print(fruits)

#diff between append() and extend()
# num = [1,2,3,4]
# num.append([5,6])
# print(num)
# #but
# num = [1,2,3,4]
# num.extend([5,6])
# print(num)


#insert()
# fruits = ["apple","banana"]
# fruits.insert(1,"mango") #inserts an element at certain index
# print(fruits)


#remove()
# fruits = ["banana","apple","banana","mango","banana"]
# fruits.remove("banana") #removes the first occurence of a value note:only removes the first match
# print(fruits)


#pop()
# fruits = ["apple","banana","mango"]
# # fruits.pop(2)#removes element by index and returns it
# fruits.pop() #without index removes the last element
# print(fruits)


# clear()
# fruits = ["apple","banana","mango"]
# fruits.clear() #removes all element from the list
# print(fruits)


#index()
# fruits = ["apple","banana","mango","banana"]
# fruits.index("banana") #this prints nothing because index does not modify the list but returns value while above methods modify the list
# print(fruits)
#you can do 
# fruits = ["apple","banana","mango","banana"]
# print(fruits.index("banana")) #returns the index of element


#count()
# fruits = ["apple","banana","mango","banana"]
# print(fruits.count("banana"))


#sort()
# fruits = ["apple","banana","mango","banana","chhery","lemon"]
# # fruits.sort() #sorts in ascending for number and alphabetically for string
# fruits.sort(reverse=True) #for sorting descending
# print(fruits)


# reverse()
# fruits = ["apple","banana","mango","banana"]
# fruits.reverse() #reverses the list order
# print(fruits)

#copy()
fruits = ["apple","banana","mango","banana"]
copyfruits = fruits.copy() #creates shallow copy of the list
print(copyfruits)


