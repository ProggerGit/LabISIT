# Ввод строки
text = input("Введите строку: ")

# Разделяем на слова
words = text.split()

# Перебираем слова и проверяем условия
print("Слова, начинающиеся на 'а' или оканчивающиеся на 'я':")
for word in words:
    if word.lower().startswith('а') or word.lower().endswith('я'):
        print(word)
