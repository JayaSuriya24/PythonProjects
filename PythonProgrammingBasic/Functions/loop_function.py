# The loop is used inside the function

def callfunction(*numbers):
    print('The loop is used inside function to perform the task ')
    # Before the addition function the total value is zero
    total=0
    for num in numbers:
        total = total + num
        print(total)

# call function one
callfunction(1,2,3,4,5)
# Call function two
callfunction(5,6,7,8,9)