while True:
    a = input('Введите первое число: ')
    b = input('Введите второе число: ')
    c = input('Введите третье число: ')
    if a.isnumeric() and b.isnumeric() and c.isnumeric():
        break
    else:
        print('Вводные данные должны быть числами!')

if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
elif a != b != c:
    print(0)
else:
    print('Непредусмотренный вариант! Сбой системы!')
