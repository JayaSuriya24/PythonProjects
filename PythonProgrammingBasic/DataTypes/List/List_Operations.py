# Slicing of a List

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print("my_list =", my_list)

# get a list with items from index 2 to index 4 (index 5 is not included)
print("my_list[2: 5] =", my_list[2: 5])

# get a list with items from index 2 to index -3 (index -2 is not included)
print("my_list[2: -2] =", my_list[2: -2])

# get a list with items from index 0 to index 2 (index 3 is not included)
print("my_list[0: 3] =", my_list[0: 3])

print('----------------------------------')

# Omitting Start and End Indices in Slicing
print("my_list =", my_list)

# get a list with items from index 5 to last
print("my_list[5: ] =", my_list[5: ])

# get a list from the first item to index -5
print("my_list[: -4] =", my_list[: -4])

# omitting both start and end index
# get a list from start to end items
print("my_list[:] =", my_list[:])

print('----------------------------------')

# Add elements to the list

# Append is used to add element in the list at last
studentName = ['a','b','d','e']
print('existing student name :',studentName)
studentName.append('c')
print('updated student list :',studentName)

print('----------------------------------')

# Add element to the list in the particular index

# Through the insert function we can add the element
# where ever we want by instructing the index value
studentNames = ['a','b','d','e']
print('existing student name :',studentNames)
studentNames.insert(2,'c')
print('updated student list :',studentNames)

print('----------------------------------')

# Add the elements fromm one list to another list

# Through the extend function we can add the elements in the different list

class1 = [1,2,3,4,5]
class2 = [6,7,8,9,10]
class3 = ['a','b','d']
class4 = ['e','f','g']

print('class-1 :',class1)
print('class-2 :',class2)

# Used to add two list of values
class1.extend(class2)

print('The updated class 1,2 :',class1)

# Inserting the value ='c' at the index of '2' at class 3
class3.insert(2,'c')

# Just add the value at the list
class4.append('h')

# Used t add two list of values
class3.extend(class4)

print('The updated class 3,4 :',class3)

print('-----------------------------------')

print('-----UPDATING THE VALUE IN THE LIST WITH INDEX-------')

# The values ar updated by annotating the index
# Using the remove function the values are removed
letters = ['a','b','c','x','y','z','l','m','n']
print('existing list of letters :',letters)
letters[3]='d'
letters[4]='e'
letters[5]='f'
print('Updated list of letters :',letters)
# remove(value that we need to remove in the list)
letters.remove('l')
letters.remove('m')
letters.remove('n')
print('Updated list of letters :',letters)

#  append()	Adds an item to the end of the list
#  extend()	Adds items of lists and other iterables to the end of the list
#  insert()	Inserts an item at the specified index
#  remove()	Removes the specified value from the list
#  pop()	Returns and removes item present at the given index
#  clear()	Removes all items from the list
#  index()	Returns the index of the first matched item
#  count()	Returns the count of the specified item in the list
#  sort()	Sorts the list in ascending/descending order
#  reverse()	Reverses the item of the list
#  copy()	Returns the shallow copy of the list