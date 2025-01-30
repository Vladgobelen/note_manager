# Импортируем необходимые модули для работы с датами
from datetime import datetime


# Функция для проверки ввода "да" или "нет"
def confirm(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response == 'да':
            return True
        elif response == 'нет' or response == '':
            return False
        else:
            print("Некорректный ввод. Пожалуйста, введите 'да' или 'нет'.")


# Функция для проверки корректного ввода даты
def input_date(prompt):
    while True:
        try:
            date_input = input(prompt)  # Запрос ввода даты
            datetime.strptime(date_input, "%d-%m-%Y")  # Проверка формата даты
            return date_input  # Возврат корректно введенной даты
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, используйте формат 'ДД-ММ-ГГГГ'.")


# Функция создания новой заметки
def create_note():
    note = {}

    note["username"] = input("Введите имя пользователя: ")

    note["titles"] = []  # Инициализация списка заголовков заметки
    print("Введите заголовки заметок (оставьте пустым для завершения):")
    while True:
        title = input("Введите заголовок заметки: ")
        if title == "":
            break  # Завершение ввода, если пользователь оставил строку пустой
        note["titles"].append(title)  # Добавление заголовка

    note["content"] = input("Введите описание заметки: ")

    # Запрос статуса заметки с проверкой на корректный ввод
    while True:
        status = input("Введите статус заметки (новая, в процессе, выполнено): ").strip().lower()
        if status in ["новая", "в процессе", "выполнено"]:
            note["status"] = status
            break
        else:
            print("Некорректный статус. Пожалуйста, введите 'новая', 'в процессе' или 'выполнено'.")

    # Автоматическое добавление текущей даты в поле created_date
    note["created_date"] = datetime.now().strftime("%d-%m-%Y")

    # Проверка корректного ввода даты истечения заметки
    note["issue_date"] = input_date("Введите дату истечения заметки в формате 'ДД-ММ-ГГГГ': ")
    return note


# Основная функция для запуска программы
def main():
    print("Добро пожаловать в 'Менеджер заметок'!\n")
    notes.append(create_note())  # Вызов функции для создания заметки
    print("Заметка создана:\n", notes)


# Запуск основной функции

if __name__ == "__main__":
    # Список для хранения всех заметок
    notes = []
    main()
