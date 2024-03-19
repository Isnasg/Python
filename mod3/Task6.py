numbers = input("Введите последовательность целых чисел через пробел: ")
numbers_list = list(map(int, numbers.split()))

has_duplicates = len(numbers_list) != len(set(numbers_list))

print(has_duplicates)