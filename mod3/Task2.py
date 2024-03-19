number = input("Введите натуральное число в десятичном коде: ")

if number.isdigit() and int(number) > 0:
    decimalnumber = int(number)

    binarynumber = bin(decimalnumber)
    octalnumber = oct(decimalnumber)
    hexadecimalnumber = hex(decimalnumber)

    print(f"Двоичное представление: {binarynumber}")
    print(f"Восьмеричное представление: {octalnumber}")
    print(f"Шестнадцатеричное представление: {hexadecimalnumber}")
else:
    print("Неверный ввод")