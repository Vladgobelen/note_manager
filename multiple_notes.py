# Импортируем необходимые модули для работы с датами
from datetime import datetime

notes = []  # Список для хранения всех заметок


# Функция для проверки корректного ввода даты
def input_date(prompt):
    while True:
        try:
            date_input = input(prompt)  # Запрос ввода даты
            datetime.strptime(date_input, "%d-%m-%Y")  # Проверка формата даты
            return date_input  # Возврат корректно введенной даты
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, используйте \
формат 'ДД-ММ-ГГГГ'.")


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


# Создание нового словаря для заметки
def create_note():
    note = {}
    note["username"] = input("Введите имя пользователя: ")

    note["titles"] = []  # Инициализация списка заголовков заметки
    print("Введите заголовки заметок (оставьте пустым для завершения):")
    while True:
        title = input("Введите заголовок заметки: ")
        if title == "":
            break  # Завершение ввода, если пользователь оставил строку пустой
        if title in note["titles"]:
            print("Этот заголовок уже существует. Пожалуйста, введите \
уникальный заголовок.")
        else:
            note["titles"].append(title)  # Добавление уникального заголовка

    note["content"] = input("Введите описание заметки: ")
    note["status"] = "Не определено"  # Установка статуса заметки по умолчанию
    # Обновление статуса только если пользователь ввел статус
    if confirm("Хотите обновить статус заметки? (да/нет): "):
        update_note_status(note)  # Вызов функции для обновления статуса зам.

    # Проверка корректного ввода даты создания заметки
    note["created_date"] = input_date("Введите дату создания заметки в \
формате 'ДД-ММ-ГГГГ': ")

    # Проверка корректного ввода даты истечения заметки
    note["issue_date"] = input_date("Введите дату истечения заметки в \
формате 'ДД-ММ-ГГГГ': ")

    notes.append(note)  # Добавление заметки в список
    print("\nЗаметка успешно добавлена!")


# Функция для отображения доступных опций статуса заметки
def display_status_options():
    print("\nВыберите текущий статус заметки:")
    print("1. Выполнено\n2. В процессе\n3. Отложено")


# Функция для обновления статуса заметки
def update_note_status(note):
    # Словарь с допустимыми статусами
    valid_statuses = {"1": "выполнено", "2": "в процессе", "3": "отложено"}
    while True:
        display_status_options()  # Вывод доступных статусов
        choice = input("Введите номер статуса либо нажмите Ввод чтобы \
оставить прежний статус: ")  # Ввод статуса
        if choice in valid_statuses:
            note["status"] = valid_statuses[choice]  # Обновление статуса
            print("Статус заметки успешно обновлён на:", note["status"])
            break
        elif choice == "":
            break  # Выход из цикла, если пользователь оставил строку пустой
        else:
            print("Некорректный ввод. Пожалуйста, выберите номер из \
предложенных вариантов.")  # Обработка некорректного ввода


# Функция проверки дедлайна
def check_deadline(note):
    current_date = datetime.now()  # Получение текущей даты
    print(f"Текущая дата: {current_date.strftime('%d-%m-%Y')}")
    while True:
        try:
            deadline = datetime.strptime(note["issue_date"], "%d-%m-%Y")
            # Вычисление количества дней до дедлайна
            days_left = (deadline - current_date).days

            if days_left < 0:
                print(f"Внимание! Дедлайн истёк {abs(days_left)} дня(ей) \
назад.")
            elif days_left == 0:
                print("Дедлайн сегодня!")
            else:
                print(f"До дедлайна осталось {days_left} дня(ей).")
            break
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, используйте \
формат 'ДД-ММ-ГГГГ'.")


# Функция для отображения всех заметок
def display_notes():
    print("\nСписок заметок:")
    for i, note in enumerate(notes, start=1):  # Перебор всех заметок в списке
        print(f"\nЗаметка номер {i}:")
        print("Имя пользователя:", note["username"])
        print("Заголовки заметки:")
        # Перебор заголовков заметки
        for j, title in enumerate(note["titles"], start=1):
            print(f'- Заголовок заметки номер {j}: {title}')
        print("Описание заметки:", note["content"])
        print("Статус заметки:", note["status"])
        print('Дата создания заметки:', note['created_date'])
        print('Дата истечения заметки:', note['issue_date'])
        check_deadline(note)  # Проверка дедлайна для каждой заметки


# Основная функция для запуска программы
def main():
    print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить \
новую заметку.")
    while True:
        create_note()  # Вызов функции для создания заметки
        if not confirm("Хотите добавить ещё одну заметку? (да/нет): "):
            break
    display_notes()  # Вывод всех заметок после завершения ввода


# Запуск основной функции
main()
