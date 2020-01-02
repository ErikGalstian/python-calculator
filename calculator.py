operators = ['+', '-', '/', '*', '%']
num1 = input('Enter the first number: \n')
if not num1.isdigit():
    print('Please enter a proper number!')
    exit()

num2 = input('Enter the second number: \n')
if not num1.isdigit():
    print('Please enter a proper number!')
    exit()

operator = input('Enter the operator: \n')
if not operator in operators:
    print('Please enter a proper operator')
    exit()


if operator == '+':
    print(float(num1) + float(num2))
elif operator == '-':
    print(float(num1) - float(num2))
elif operator == '/':
    print(float(num1) / float(num2))
elif operator == '*':
    print(float(num1) * float(num2))
elif operator == '%':
    print(float(num1) % float(num2))


