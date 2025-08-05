
number1 = int(input('Enter the First number :'))
number2 = int(input('Enter the Second number :'))


print('----------')
print('Assignment')
print('----------')
# a = number1 which is number1 is assigned to variable 'a' with '=' Operator
# b = number2 which is number2 is assigned to variable 'b' with '=' Operator
a = number1
b = number2
c = a + b
print(c)

print('----------')
print('Addition Assignment')
print('----------')
# a1 += b1  Explanation of this line is  a1 = a1 + b1
# The value of the variable is added with another value and storing in the existing variable
a1 = number1
b1 = number2
print('Before a1 & b1 value is :',a1 ,'&' ,b1)
a1 += b1 # a1 = a1 + b1 (----New a1 value is used in next statement------)
b1 += a1 # b1 = b1 + a1
print('After a1 & b1 value is :',a1,'&',b1)


print('----------')
print('Subtraction Assignment')
print('----------')
# a2 -= b2  Explanation of this line is  a2 = a2 + b2
# The value of the variable is subtracted with another value and storing in the existing variable
a2 = number1
b2 = number2
print('Before a2 & b2 value is :',a2 ,'&' ,b2)
a2 -= b2 # a2 = a2 - b2 (----New a2 value is used in next statement------)
b2 -= a2 # b2 = b2 - a2
print('After a2 & b2 value is :',a2,'&',b2)


print('----------')
print('Multiplication Assignment')
print('----------')
# a3 *= b3  Explanation of this line is  a3 = a3 * b3
# The value of the variable is multiplied with another value and storing in the existing variable
a3 = number1
b3 = number2
print('Before a3 & b3 value is :',a3 ,'&' ,b3)
a3 *= b3 # a3 = a3 * b3 (----New a3 value is used in next statement------)
b3 *= a3 # b3 = b3 * a3
print('After a3 & b3 value is :',a3,'&',b3)


print('----------')
print('Division Assignment')
print('----------')
# a4 /= b4  Explanation of this line is  a4 = a4 / b4
# The value of the variable is divided with another value and storing in the existing variable
a4 = number1
b4 = number2
print('Before a4 & b4 value is :',a4 ,'&' ,b4)
a4 /= b4 # a4 = a4 / b4 (----New a1 value is used in next statement------)
b4 /= a4 # b4 = b4 / a4
print('After a4 & b4 value is :',a4,'&',b4)


print('----------')
print('Remainder Assignment')
print('----------')
# a5 %= b5  Explanation of this line is  a5 = a5 % b5
# The value of the variable is added with another value and storing in the existing variable
a5 = number1
b5 = number2
print('Before a5 & b5 value is :',a5 ,'&' ,b5)
a5 %= b5 # a5 = a5 % b5 (----New a1 value is used in next statement------)
b5 %= a5 # b5 = b5 % a5
print('After a5 & b5 value is :',a5,'&',b5)


print('----------')
print('Exponent Assignment')
print('----------')
# a6 += b6  Explanation of this line is  a6 = a6 + b6
# The value of the variable is added with another value and storing in the existing variable
a6 = number1
b6 = number2
print('Before a6 & b6 value is :',a6 ,'&' ,b6)
a6 **= b6 # a6 = a6 ** b6 (----New a1 value is used in next statement------)
b6 **= a6 # b6 = b6 ** a6
print('After a6 & b6 value is :',a6,'&',b6)