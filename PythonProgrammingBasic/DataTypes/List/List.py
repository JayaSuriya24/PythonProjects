#Ordered - They maintain the order of elements.
#Mutable - Items can be changed after creation.
#Allow duplicates - They can contain duplicate values.


# List of three elements
numbers = [19, 26, 29]
print(numbers)

# In FOR-LOOP
for num in numbers:
    print(num)

# List of items in different data types
# List containing strings, numbers and another list
student = ['Suriya', 24, 'Computer Science', [2, 4]]
print(student)

# Empty list
empty_list = []
print(empty_list)


#Each element in a list is associated with a number, known as an index.
# The index of first item is 0, the index of second item is 1, and so on.

brother_names = ['Hari','Guhan','Sudhaman']

#access the first element
print('brother name in index(0) is :',brother_names[0])

#access the second element
print('brother name in index(1) is :',brother_names[1])

#access the third element
print('brother name in index(2) is :',brother_names[2])

print('------------------------------------------------')
#Using negative index

#access the first element
print('brother name in index(-3) is :',brother_names[-3])

#access the second element
print('brother name in index(-2) is :',brother_names[-2])

#access the third element
print('brother name in index(-1) is :',brother_names[-1])