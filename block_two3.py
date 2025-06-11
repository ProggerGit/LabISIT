import os
import glob
import subprocess

def open_file():
    path = input("Введите путь к файлу: ")
    if os.path.isfile(path):
        try:
            subprocess.run(["notepad" if os.name == "nt" else "nano", path])
        except Exception as e:
            print(f"Ошибка при открытии: {e}")
    else:
        print("Файл не найден.")

def show_file_content():
    path = input("Введите путь к файлу: ")
    if os.path.isfile(path):
        with open(path, 'r', encoding="utf-8") as f:
            print("\n--- Содержимое файла ---")
            print(f.read())
    else:
        print("Файл не найден.")

def find_files():
    pattern = input("Введите полное или частичное имя файла (можно с *): ")
    matches = glob.glob(f"**/{pattern}", recursive=True)
    if matches:
        print("\nНайденные файлы:")
        for match in matches:
            print(os.path.abspath(match))
    else:
        print("Файлы не найдены.")

def list_directory():
    path = input("Введите путь к директории: ")
    if os.path.isdir(path):
        print(f"\nСодержимое {path}:")
        for item in os.listdir(path):
            print(item)
    else:
        print("Директория не найдена.")

# Главное меню
def main():
    while True:
        print("\n📁 Консольный файловый менеджер")
        print("1 – Открыть файл")
        print("2 – Показать содержимое файла")
        print("3 – Найти файл/файлы")
        print("4 – Раскрыть директорию")
        print("0 – Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            open_file()
        elif choice == "2":
            show_file_content()
        elif choice == "3":
            find_files()
        elif choice == "4":
            list_directory()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Повторите.")

# Запуск программы
if __name__ == "__main__":
    main()
