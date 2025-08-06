#  The primary difference is that we cannot modify a tuple once it is created.

number = [1, 2, 3, 4]
print('Numbers :',number)

tuple_numbers = tuple((1,2,3,4))
print('Tuple Numbers :',tuple_numbers)

print('-----------------------------------------------------')
print('NORMAL LIST VALUES CAN BE CHANGE WITH THE INDEX VALUE')
print('-----------------------------------------------------')

print('Existing Number :',number)
number[3]=0
print('Updated Numbers :',number)

print('-------------------------------')
print('TUPLE VALUES CAN NOT BE CHANGED')
print('-------------------------------')
