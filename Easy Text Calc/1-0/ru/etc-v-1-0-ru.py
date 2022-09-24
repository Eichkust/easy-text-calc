print("*"*15,"Простой Калькулятор v.0.1-beta","*"*15)
print('Примечание: Для выхода напишите q в качестве знака.')

while True:
    s = input('Главное меню\n(*,/,-,+)/q (Для выхода из программы)\nЗнак: ')
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
                print('Делить на ноль по правилам математики запрещено!')
    else:
        print('Это неверный знак!')