def main():
    print('Привет!')

    text_1 = 'nPuBet_MUP'
    text_2 = 'Ботать_это круто'
    text_3 = '1,2,3,4'
    text_4_1 = '1234*&%1$'
    text_4_2 = '____abc1234____'
    text_5 = '.......PyThon;is; AWESome....'

    while True: 
        print('Достпуные уровни:')
        print('1. Уровень 1 (upper, lower, capitalize)')
        print('2. Уровень 2 (find, replace, count, index)')
        print('3. Уровень 3 (split, join)')
        print('4. Уровень 4 (isdigit, isalpha, strip, format)')
        print('5. Уровень 5 (Тест строки)')
        print('0. Выход из программы')

        c = input('Выберите номер уровня (0-5): ').strip()
        if c == '0':
            print('Пока :)')
            break
        elif c == '1':
            print('Уровень 1. Исходный текст: ', text_1)

            print('upper:')
            print(text_1.upper())

            print('lower:')
            print(text_1.lower())

            print('capitalize:')
            print(text_1.capitalize())
        elif c == '2':
            print('Уровень 2. Исходный текст: ', text_2)

            print('find:')
            a = input('Что найти? -> ')
            print(text_2.find(a))

            print('replace:')
            a = input('Что заменить? -> ')
            b = input('На что? -> ')
            print(text_2.replace(a, b))

            print('count:')
            a = input('Что подсчитать? -> ')
            print(text_2.count(a))

            # !!!
            print('index:')
            a = input('Чей индекс найти? -> ')
            try:
                print(text_2.index(a))
            except:
                print('Такого символа в строке нет')
        elif c == '3':
            print('Уровень 3. Исходный текст: ', text_3)

            print('split:')
            a = input('На что поделить? -> ')
            print(text_3.split(a))

            print('join:')
            b = input('С чем объединить? -> ')
            print((text_3.split(a)).join(b))
        elif c == '4':
            print('Уровень 4. Исходный текст 1: ', text_4_1, ' /// Исходный текст 2: ', text_4_2)

            print('isdigit:')
            print(text_4_1.isdigit())

            print('isalpha:')
            print(text_4_1.isalpha())

            print('strip:')
            a = input('Какие символы удалить? -> ')
            print(text_4_2.strip())

            print('format:')
            a = input('Что вставить в шаблон? -> ')
            print(f'format, {text_4_2}, {a}')
            
        elif c == '5':
            print('Уровень 5. Исходный текст: ', text_5)

            print('Тест строки:')
            print('strip("."):')
            print(text_5.strip("."))
            print('lower:')
            print(text_5.lower())
            print('upper:')
            print(text_5.upper())

        else:
            print('Неизвестный номер уровня')

main()