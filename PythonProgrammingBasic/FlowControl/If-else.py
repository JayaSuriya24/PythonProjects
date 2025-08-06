# If the if-condition fails program directly moved to the else-condition

number = int(input('Enter a number: '))

# Checking the condition in if-condition (The given input is greater than zero or not)
if number > 0:
    print('Positive number')
    # if-condition is false else part will execute
else:
    print('Not a positive number')

# This line is out of if statement
print("This statement always executes")