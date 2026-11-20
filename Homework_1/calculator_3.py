def calculate(a, b, o):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/':
        if b != 0:
            return a / b
        else:
            return 'Ошибка. Деление на ноль невозможно'
    else:
        return 'Неизвестная операця'

while True:
    print('Если вы хотите остановить расчет, то в любой момент введите "."')
    n1 = float(input('Введите первое число: '))
    if n1 == '.':
        print('Расчет остановлен')
        break
    op = input('Введите операцию (+, -, *, /): ')
    if op == '.':
        print('Расчет остановлен')
        break
    n2 = float(input('Введите второе число: '))
    if n2 == '.':
        print('Расчет остановлен')
        break

    result = calculate(n1, n2, op)
    print('Результат: ', result)