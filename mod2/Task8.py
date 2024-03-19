def generate_new_word(words):
    new_word = ""
    for word in words:
        new_word += word[-1]
    return new_word

# Пример использования
word_list = input("Введите список слов через пробел: ").split()
new_word = generate_new_word(word_list)
print("Слово из последних букв каждого слова:", new_word)