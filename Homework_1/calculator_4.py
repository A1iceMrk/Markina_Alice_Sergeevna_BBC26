class Calculator:
    def __init__(self):
        pass
    def run(self):
        a = float(input('Введите первое число: '))
        o = input('Введите операцию (+, -, *, /): ')
        b = float(input('Введите второе число: '))

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

calc = Calculator()
print('Результат: ', calc.run())