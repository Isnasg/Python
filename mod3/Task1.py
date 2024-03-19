a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

# Сортируем числа по возрастанию
sorted_numbers = sorted([a, b, c])

# Находим число, стоящее между двумя другими
middle_number = sorted_numbers[1]

print(f"Числа {a}, {b}, {c} упорядочены по возрастанию: {sorted_numbers}")
print(f"Число, стоящее между двумя другими: {middle_number}")