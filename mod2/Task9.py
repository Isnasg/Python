def cleanphonenumber(phone):
    cleanchars = ['+', '-', ')', '(', ' ']
    for char in cleanchars:
        phone = phone.replace(char, '')
    return phone

# Пример использования
phonenumber = input("Введите номер телефона с различными символами: ")
cleanednumber = cleanphonenumber(phonenumber)
print("Очищенный номер телефона:", cleanednumber)