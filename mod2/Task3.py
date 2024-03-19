numbers = input("Введите три числа через пробел: ")
numbers_list = list(map(int, numbers.split()))

numbers_list.sort()

print(f"Число на второй позиции: {numbers_list[1]}")