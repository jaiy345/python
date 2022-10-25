#Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
from itertools import count


first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
inter=first_set.intersection(second_set)
for item in inter:
    first_set.remove(item)
print(first_set)
print(second_set)
    
        








            