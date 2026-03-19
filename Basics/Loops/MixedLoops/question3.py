# Write code using BOTH loops to find all COMMON ELEMENTS between two lists.
# list1 = [1, 3, 5, 7, 9, 11, 15]
# list2 = [3, 6, 9, 12, 15, 18]
# Use for loop on list1 and while loop to search through list2.

# list1 = [1, 3, 5, 7, 9, 11, 15]
# list2 = [3, 6, 9, 12, 15, 18]

# newlist = []

# for num in list1:        
#     j = 0
#     while j < len(list2):   
#         if num == list2[j]:
#             newlist.append(num) 
#             break
#         j += 1

# print(newlist)


#What if the list has duplicates
list1 = [1, 3, 5, 9,7, 9, 11, 15]
list2 = [3, 6, 9, 12, 15, 18]
newlist = []

for num in list1:
    if num in newlist:   # skip duplicates
        continue
        
    j = 0
    while j < len(list2):
        if num == list2[j]:
            newlist.append(num)
            break
        j += 1

print(newlist)
        