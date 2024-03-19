def countcharsatbeginning(s, i):
    count = 0
    for char in s:
        if char == i:
            count += 1
        else:
            break
    return count

# Пример использования
s = input("Введите строку: ")
i = input("Введите символ: ")
result = countcharsatbeginning(s, i)
print(f"Количество символов '{i}' в начале строки: {result}")