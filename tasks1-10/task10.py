while True:
    n = input()

    if n.lower() == 'стоп':
        print('Программа завершена')
        break
    try:
        number = float(n)
        print(number)
    except ValueError:
        print('Введите число или "стоп"!')