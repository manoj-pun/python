# You have two lists: list_a = [1, 2, 3, 4, 5, 6] and list_b = [4, 5, 6, 7, 8, 9]. First, do set operations:
# find the union, intersection, and elements only in list_a. Then repeat everything using only list
# comprehensions (no set). Print results from both approaches and confirm they match.

list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8, 9]

# --- Set approach ---
set_a = set(list_a)
set_b = set(list_b)

union_set = set_a | set_b
intersection_set = set_a & set_b
only_a_set = set_a - set_b

print("Set results")
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Only in list_a:", only_a_set)


# --- List comprehension approach ---
union_list = list_a + [x for x in list_b if x not in list_a]
intersection_list = [x for x in list_a if x in list_b]
only_a_list = [x for x in list_a if x not in list_b]

print("\nList comprehension results")
print("Union:", union_list)
print("Intersection:", intersection_list)
print("Only in list_a:", only_a_list)





