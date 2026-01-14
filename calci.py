number1 = input("Enter first number:")
num1 = int(number1)
sign = input('Enter the sign:')
number2 = input("Enter second number:")
num2 = int(number2)
if sign == '+':
    print('The result is: ' + str(num1 = num2))
elif sign == '-':
    print('The result is: ' + str(num1 - num2))
elif sign == '*':
    print('The result is: ' + str(num1 * num2))
elif sign == '/':
    print('The result is: ' + str(num1 / num2))
else:
    print('Input is invalid please enter either +,-,*,/')
