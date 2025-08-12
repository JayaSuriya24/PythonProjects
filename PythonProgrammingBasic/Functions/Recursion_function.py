# Recursion function can call the function itself

def fun(num):

    if num == 1:
        return 1
    else:
        return (num * fun(num - 1))

number = int(input('Enter the number:'))
fun(number)
print('Factorial of',number,'is',fun(number))
