print("*"*15,"Simple Text Calculator v.1.2","*"*15)
print('Note: To exit the program, type Q or q in the Sign line.')
print("What's new in version 1.2\nAdded the ability to raise to a power.\nTo do this, enter ** in the Sign line")
print('Patch 1.2 is firmware, but there may be errors in the program. Be carefull')
while True:
    s = input('Permissible Signs \n (*,/,-,+,**)\n Sign: ')
    if s == 'q' or s == 'Q':
        print(' End of program!')
        break
    if s in ('*', '/', '-', '+', '**'):
        x = float(input(' x = '))
        y = float(input(' y = '))
        if s == '+':
            print(' %.2f' % (x+y))
        elif s == '-':
            print(' %.2f' % (x-y))
        elif s == '*':
            print(' %.2f' % (x*y))
        elif s == '**':
            print(' %.2f' % (x**y))
        elif s == '/':
            if y != 0:
                print(' %.2f' % (x / y))
            else:
                print(' Division by zero is forbidden by the rules of mathematics!')
    else:
        if s == '':
            print(' You display a pass, but you need a sign!')
        else:
            print(' This is the wrong sign!')