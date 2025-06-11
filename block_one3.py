import pickle

# --- Функция для задачи 1 ---
def auto_sales_task():
    car_sales = {
        "Toyota":   {"Россия": 12000, "США": 35000, "Китай": 28000, "Германия": 14000, "Франция": 13000, "Япония": 50000},
        "BMW":      {"Россия": 8000,  "США": 20000, "Китай": 15000, "Германия": 40000, "Франция": 10000, "Япония": 12000},
        "Ford":     {"Россия": 9000,  "США": 45000, "Китай": 22000, "Германия": 10000, "Франция": 9000,  "Япония": 8000},
        "Kia":      {"Россия": 10000, "США": 16000, "Китай": 13000, "Германия": 6000,  "Франция": 5000,  "Япония": 11000},
        "Hyundai":  {"Россия": 9500,  "США": 17000, "Китай": 14000, "Германия": 7000,  "Франция": 4000,  "Япония": 12000},
        "Chevrolet":{"Россия": 8500,  "США": 30000, "Китай": 18000, "Германия": 7000,  "Франция": 6000,  "Япония": 9000},
        "Lada":     {"Россия": 40000, "США": 1000,  "Китай": 500,   "Германия": 2000,  "Франция": 1500,  "Япония": 700}
    }

    print("\nСписок автомобилей и суммарные продажи:")
    for brand, countries in car_sales.items():
        total = sum(countries.values())
        print(f"{brand}: {total} шт.")

    print("\nМаксимальные и минимальные продажи по странам:")
    for brand, countries in car_sales.items():
        max_country = max(countries, key=countries.get)
        min_country = min(countries, key=countries.get)
        print(f"{brand}: Макс — {max_country} ({countries[max_country]}), Мин — {min_country} ({countries[min_country]})")

    print("\nПродажи в России:")
    for brand in car_sales:
        print(f"{brand}: {car_sales[brand]['Россия']} шт.")

    print("\nАвто, где продажи в США > Китая более чем на 20%:")
    for brand, countries in car_sales.items():
        us = countries["США"]
        cn = countries["Китай"]
        if us > cn * 1.2:
            print(f"{brand}: США — {us}, Китай — {cn}")

    # Сохраняем в бинарный файл
    with open("data.pickle", "wb") as f:
        pickle.dump(car_sales, f)
    print("\nДанные сохранены в 'data.pickle'.")

    # Проверка загрузки
    with open("data.pickle", "rb") as f:
        loaded = pickle.load(f)
    print("\nЗагруженные данные из файла:")
    for brand, sales in loaded.items():
        print(f"{brand}: {sales}")


# --- Функция для задачи 2 ---
def text_analysis_task():
    def starts_with_vowel(word):
        return word[0].lower() in "аеёиоуыэюяaeiou"

    try:
        with open("input.txt", "r", encoding="utf-8") as infile, \
             open("output.txt", "w", encoding="utf-8") as outfile:
            for line in infile:
                words = line.strip().split()
                count = sum(1 for word in words if word and starts_with_vowel(word))
                outfile.write(f"{count}\n")
        print("\nАнализ завершён. Результаты записаны в 'output.txt'.")
    except FileNotFoundError:
        print("\nОшибка: файл 'input.txt' не найден.")


# --- Главное меню ---
def main():
    while True:
        print("\nВыберите действие:")
        print("1 — Работа с автопродажами и pickle")
        print("2 — Анализ текстового файла (input.txt → output.txt)")
        print("0 — Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            auto_sales_task()
        elif choice == "2":
            text_analysis_task()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Повторите попытку.")

# --- Запуск ---
main()
