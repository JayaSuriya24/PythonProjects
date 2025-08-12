# Local variable
# the variable is created and used inside the function is called as local variable

def fun1():

    name='suriya'

    print('My name is ',name)

fun1()

print('--------------------------------')
# Global variable
# If the variable is created outside thr function or method  which is used as a global variable

name = 'Jaya Suriya'

def fun2():

    print('My full name is ',name)

fun2()

print('--------------------------------')

# NonLocal variable
# The local V can change into the global V through the nonlocal keyword

def outerfun():
    #intial text in outer function
    text = 'Suriya'
    def innerfun():
        # local V  to  global V by (nonlocal key word)
        nonlocal text
        # call outer variable
        print('Inner text',text)
        # Change the value of outer V
        text = 'Jaya Suriya'
    # Inner call function
    innerfun()
    print('outer text', text)
# Outer call function
outerfun()
