def Calculator():
    print('----simple calculator----')


    try:
        num1=float(input('enter num1:'))
        num2=float(input('enter num2:'))
        op= input('operator(+,-,*,/):')

        if op == '+':
            result=num1+num2
        elif op == '-':
            result=num1-num2
        elif op == '*':
            result=num1*num2
        elif op =='/':
            if num2==0:
             print('error:cannot be divided by zero')
            return
            result =num1/num2
        else:
            print('invalid operator')
            return
        print(f'Result:{num1}{op}{num2}={result}')

    except ValueError:
        print('please enter the valid number!')

Calculator()
     
        