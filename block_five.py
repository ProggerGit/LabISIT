# --- Рекурсивная функция для суммы цифр ---
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

# --- Функция подсчета делителей числа ---
def count_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

# --- Задача 1: Числа с макс. кол-вом делителей ---
def task1():
    M = int(input("Введите начало интервала M: "))
    N = int(input("Введите конец интервала N: "))

    max_divisors = 0
    numbers_with_max_divs = []

    for num in range(M, N + 1):
        divs = count_divisors(num)
        if divs > max_divisors:
            max_divisors = divs
            numbers_with_max_divs = [num]
        elif divs == max_divisors:
            numbers_with_max_divs.append(num)

    print(f"\nЧисла с наибольшим количеством делителей ({max_divisors}): {numbers_with_max_divs}")

# --- Задача 2: Рекурсивная сумма цифр ---
def task2():
    number = int(input("Введите натуральное число: "))
    print(f"Сумма цифр: {sum_of_digits(number)}")

# --- Главное меню ---
def main():
    while True:
        print("\nВыберите задачу:")
        print("1 — Найти числа с наибольшим числом делителей в [M, N]")
        print("2 — Рекурсивная сумма цифр натурального числа")
        print("0 — Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск программы
main()
