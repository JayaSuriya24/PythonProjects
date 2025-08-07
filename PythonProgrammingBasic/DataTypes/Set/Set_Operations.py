#   Built-in Functions with Set

#  all()	Returns True if all elements of the set are true (or if the set is empty).
#  any()	Returns True if any element of the set is true. If the set is empty, returns False.
#  enumerate()	Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
#  len()	Returns the length (the number of items) in the set.
#  max()	Returns the largest item in the set.
#  min()	Returns the smallest item in the set.
#  sorted()	Returns a new sorted list from elements in the set(does not sort the set itself).
#  sum()	Returns the sum of all elements in the set.

# Add Items in set
number = {1,2,3,4,5,6}
print('number :',number)
print('Existing Number is :',number)
number.add(7)
print('Updated Number is :',number)
# Update Items in set
number2 = [7,8,7,9,10]
print('number2 :',number2)
number.update(number2)
print(number,"Number after the update")
# Delete Items in set
number.remove(10)
print(number,'Number after the deletion ')

# Iterate over in set
fruits = {"Apple", "Peach", "Mango"}
# for loop to access each fruits
for fruit in fruits:
    print(fruit)

# Number of elements in set
even_numbers = {2,4,6,8}
print('Set:',even_numbers)
# find number of elements
print('Total Elements:', len(even_numbers))

# Union of two set
# first set
A = {1, 3, 5}
# second set
B = {0, 2, 4}
# perform union operation using |
print('Union using |:', A | B)
# perform union operation using union()
print('Union using union():', A.union(B))


# Set intersection
# first set
A1 = {1, 3, 5}
# second set
B1 = {1, 2, 3}
# perform intersection operation using &
print('Intersection using &:', A1 & B1)
# perform intersection operation using intersection()
print('Intersection using intersection():', A1.intersection(B1))


# Difference between two sets
# first set
A2 = {2, 3, 5}
# second set
B2 = {1, 2, 6}
# perform difference operation using &
print('Difference using &:', A2 - B2)
# perform difference operation using difference()
print('Difference using difference():', A2.difference(B2))


# Set symmetric difference
# first set
A3 = {2, 3, 5}
# second set
B3 = {1, 2, 6}
# perform difference operation using &
print('using ^:', A3 ^ B3)
# using symmetric_difference()
print('using symmetric_difference():', A3.symmetric_difference(B3))

# Check two sets are equal
# first set
A4 = {1, 3, 5}
# second set
B4 = {3, 5, 1}
# perform difference operation using &
if A4 == B4:
    print('Set A4 and Set B4 are equal')
else:
    print('Set A4 and Set B4 are not equal')

# Other set methods

#add()	Adds an element to the set
#  clear()	Removes all elements from the set
#  copy()	Returns a copy of the set
#  difference()	Returns the difference of two or more sets as a new set
#  difference_update()	Removes all elements of another set from this set
#  discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
#  intersection()	Returns the intersection of two sets as a new set
#  intersection_update()	Updates the set with the intersection of itself and another
#  isdisjoint()	Returns True if two sets have a null intersection
#  issubset()	Returns True if another set contains this set
#  issuperset()	Returns True if this set contains another set
#  pop()	Removes and returns an arbitrary set element. Raises KeyError if the set is empty
#  remove()	Removes an element from the set. If the element is not a member, raises a KeyError
#  symmetric_difference()	Returns the symmetric difference of two sets as a new set
#  symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
#  union()	Returns the union of sets in a new set
#   update()	Updates the set with the union of itself and others