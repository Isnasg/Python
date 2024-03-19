num = input("Введите натуральное число в десятичном коде: ")

if num.isdigit() and int(num) > 0:
    num = int(num)

    # Для двоичного кода
    binary_num = ""
    while num > 0:
        remainder = num % 2
        binary_num = str(remainder) + binary_num
        num = num // 2

    # Для восьмеричного кода
    octal_num = ""
    num = int(num)
    while num > 0:
        remainder = num % 8
        octal_num = str(remainder) + octal_num
        num = num // 8

    # Для шестнадцатеричного кода
    hex_num = ""
    hex_values = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while num > 0:
        remainder = num % 16
        if remainder in hex_values:
            hex_num = hex_values[remainder] + hex_num
        else:
            hex_num = str(remainder) + hex_num
        num = num // 16

    print(f"Двоичный код: {binary_num}")
    print(f"Восьмеричный код: {octal_num}")
    print(f"Шестнадцатеричный код: {hex_num}")

else:
    print("Неверный ввод")