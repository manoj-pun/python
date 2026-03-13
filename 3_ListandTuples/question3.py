# Write a function rotate_list(lst, n) that shifts every element n positions to the right.
# rotate_list([1,2,3,4,5], 2) should give [4,5,1,2,3]. Make it work for any n, including n bigger than
# the list length and negative n (left rotation).

def rotate_list(lst, n):
    if len(lst) == 0:
        return lst

    n = n % len(lst)   # normalize rotation
    return lst[-n:] + lst[:-n]

# print(rotate_list([1,2,3,4,5], 2))

# print(rotate_list([1,2,3,4,5], 7))#rotate bigger than the length

print(rotate_list([1,2,3,4,5], -2)) #left rotation