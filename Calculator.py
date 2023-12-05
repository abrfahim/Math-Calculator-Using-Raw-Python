print('Simple Calculator Using Python')

try:
    x = float(input("Enter first number:   "))
    y = float(input('Enter second number:  '))
except ValueError as err:
    print('Find an error: ', err)


select = str(input('Select any operand to calculate: \n Add (+), Substract(-), Multiply(*), Divid(/) \n Modulus(%), Exponential(**), Floor Divid(//) :'))

try:
    if select == '+':
        print(f'{x} + {y} =:', x + y)
    elif select == '-':
        print(f'{x} - {y} =:',x - y)
    elif select == '*':
        print(f'{x} * {y} =:',x * y)
    elif select == '/':
        print(f'{x} / {y} =:',x / y)
    elif select == '%':
        print(f'{x} % {y} =:',x % y)
    elif select == '**':
        print(f'{x} ** {y} =:',x ** y)
    elif select == '//':
        print(f'{x} // {y} =:',x // y)
    else:
        print('Invalid Operator, You Must Select an Operator.')
except ValueError and ZeroDivisionError as err:
    print("Find an error:", err)