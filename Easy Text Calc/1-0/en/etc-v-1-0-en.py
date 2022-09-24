print("*"*15,"Easy Text Calc v.0.1-beta","*"*15)
print('Note: To exit, write "q" as a sign.')

while True:
    s = input('Main Menu:\n(*,/,-,+)/q (To exit the program)\nSign: ')
    if s == 'q': break;
    if s in ('*', '/', '-', '+'):
        x = float(input('x= '))
        y = float(input('y= '))
        if s == '+':
            print('%.2f' % (x+y))
        elif s == '-':
            print('%.2f' % (x-y))
        elif s == '*':
            print('%.2f' % (x*y))
        elif s == '/':
            if x != 0:
                print('%.2f' % (x / y))
            else:
                print('Dividing by zero is forbidden by the rules of mathematics!')
    else:
        print('This is the wrong sign!')