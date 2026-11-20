def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def multiply(a, b):
    return a * b
def devide(a, b):
    if b != 0:
        return a / b
    else:
        return 'Ошибка. Невозможно деление на ноль'

n1 = float(input('Введите первое число: '))
op = input('Введите операцию (+, -, *, /): ')
n2 = float(input('Введите второе число: '))

if op == '+':
    print('Результат: ', plus(n1, n2))
elif op == '-':
    print('Результат: ', minus(n1, n2))
elif op == '*':
    print('Результат: ', multiply(n1, n2))
elif op == '/':
    print('Результат: ', devide(n1, n2))
else:
    print('Неизвестная операця')