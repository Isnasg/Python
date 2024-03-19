def checknumbers(numberslist):
    uniquenumbers = set(numberslist)
    if len(uniquenumbers) == 1:
        print("Все числа равны")
    elif len(uniquenumbers) == len(numberslist):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

numbers = input("Введите список чисел через пробел: ").split()
numbers = list(map(int, numbers))

checknumbers(numbers)