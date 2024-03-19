def checkzerosandones(s):
    count0 = s.count('0')
    count1 = s.count('1')

    if count0 == count1:
        return 'yes'
    else:
        return 'no'


# Пример использования
s = input("Введите строку из 0 и 1: ")
result = checkzerosandones(s)
print(result)
