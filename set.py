"""
    Student ID = 20CE068
    STUDENT NAME = PANCAHAL JAY MANOJKUMAR
   a. Write a Python program to add member(s) in a set and clear a set

    b. Write a Python program to remove an item from a set if it is present in the set.

    c. Write a Python program to create an intersection, Union, difference of sets.

    d. Write a Python program to find maximum and the minimum value in a set.

    e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

                    GITHUB REPORSITORY LINK = https://githubcom./jaypanchal1706/python_assigment1.git

"""

# A. Write a Python program to add member in a set and clear a set

set = {'H', 'e', 'l', 'l', 'o'}
set.add('!')
print("Letters: ", set)
print("Set after clear: ", set.clear())

# B. Write a program to remove an item from a set if it is present in the set

set = {'P','Y','T','H','O','N'}
set.remove('H')
print("After removing itme from the set :",set)

# C. Write a program to create an intersection , union , different from set.

set1 = {1, 3,5,6,7,9}
set2 = {4,5,7, 10, 12, 9, 8}
print("Union of A and B: ", set1.union(set2))
print("Intersection of A and B: ", set1.intersection(set2))
print("Difference of A and B: ", set1.difference(set2), set2.difference(set1))

# D. Write a program to find maximum and the minimum value in a set.
set = {138, 290, 330, 409, 580,345,232,983}
print("Minimum value: ", min(set))
print("Maximum value: ", max(set))


#E.   Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

def findcommon(items):
    tracker = {}
    for item in items:
        if item not in tracker.keys():
            tracker[item] = 0
        tracker[item] = tracker[item] + 1
    maxitem = None
    max = -1
    for key in tracker.keys():
        if (tracker[key]) > max:
            max = tracker[key]
            maxitem = key
    return maxitem


l1 = [1, 2, 3, 2, 3, 2, 4, 5, 6,7,8]
tuple1 = ("apple", "banana", "apple", "mango")

print("Common in List: ", findcommon(l1))
print("Common in Tuple: ", findcommon(tuple1))



