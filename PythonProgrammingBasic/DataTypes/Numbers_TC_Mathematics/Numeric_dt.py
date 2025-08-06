num1 = 5
print(num1, 'is of type', type(num1))

num2 = 5.42
print(num2, 'is of type', type(num2))

num3 = 8+2j
print(num3, 'is of type', type(num3))

print('------------------------------------')

# When we get the general input from the user

number1 = input('Enter the int value :')
print(number1, 'is of type', type(number1))

number2 = input('Enter the float value :')
print(number2, 'is of type', type(number2))

number3 = input('Enter the complex value :')
print(number3, 'is of type', type(number3))

print('------------------------------------')

# When we get the TypeConvertion input from the user

number4 = int(input('Enter the int value :'))
print(number4, 'is of type', type(number4))

number5 = float(input('Enter the float value :'))
print(number5, 'is of type', type(number5))

number6 = complex(input('Enter the complex value :'))
print(number6, 'is of type', type(number6))