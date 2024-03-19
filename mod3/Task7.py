phonenumber = input("Введите номер телефона: ")

cleanedphonenumber = ''.join(char for char in phonenumber if char.isdigit())

print(f"Очищенный номер телефона: {cleanedphonenumber}")