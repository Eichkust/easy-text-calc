print("*"*15,"Простой Калькулятор v.1.2","*"*15)
print('Примечание: Для выхода из программы напишите Q или q в строке Знак.')
print('Нововведения в версии 1.2\nДобавлена возможность возводить в степень.\nДля этого введите ** в строке Знак')
print('Патч 1.2 прошивен, но могут появляться ошибки в работе программы. Будьте бдительны')
while True:
    s = input('Допустимые Знаки \n (*,/,-,+,**)\n Знак: ')
    if s == 'q' or s == 'Q':
        print(' Конец программы!')
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
                print(' Деление на ноль по правилам математики запрещена!')
    else:
        if s == '':
            print(' Ты выводишь пропуск, а надо знак!')
        else:
            print(' Это неверный знак!')