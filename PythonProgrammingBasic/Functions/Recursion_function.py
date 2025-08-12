# Recursion function can call the function itself

# This is a recursive function to find the factorial of an integer

def fun(num):

    if num == 1:
        return 1
    else:
        return (num * fun(num - 1))

number = int(input('Enter the number:'))
fun(number)
print('Factorial of',number,'is',fun(number))

# factorial(3)          # 1st call with 3
# 3 * factorial(2)      # 2nd call with 2
# 3 * 2 * factorial(1)  # 3rd call with 1
# 3 * 2 * 1             # return from 3rd call as number=1
# 3 * 2                 # return from 2nd call
# 6                     # return from 1st call
