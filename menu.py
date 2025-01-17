# Импортируем необходимые модули
from colorama import Fore, Style, init
from create_note_function import create_note
from update_note_function import update_note
from display_notes_function import display_notes
from delete_note import delete_notes
from search_notes_function import choice_search

# Инициализация colorama для работы с цветным текстом в консоли
init(autoreset=True)


def choice_note(notes):
    """
    Функция для выбора заметки по её номеру.
    :param notes: Список заметок.
    :return: Индекс выбранной заметки в списке.
    """
    check_size = len(notes)
    while True:
        try:
            my_note = int(input("Введите номер заметки, которую нужно изменить: "))
            if 1 <= my_note <= check_size:
                return my_note - 1  # Возвращаем индекс (нумерация с 0)
            else:
                print("Такой заметки не существует")
        except ValueError:
            print("Введите номер заметки - число")


def handle_create_note(notes):
    """
    Обработка создания новой заметки.
    :param notes: Список заметок.
    """
    notes.append(create_note())
    print(Fore.GREEN + "Заметка создана!" + Style.RESET_ALL)


def handle_update_note(notes):
    """
    Обработка обновления существующей заметки.
    :param notes: Список заметок.
    """
    if notes:
        note_index = choice_note(notes)
        update_note(notes[note_index])
        print(Fore.GREEN + "Заметка обновлена!" + Style.RESET_ALL)
    else:
        print("Нет заметок для изменения")


def handle_delete_note(notes):
    """
    Обработка удаления заметки.
    :param notes: Список заметок.
    :return: Обновлённый список заметок после удаления.
    """
    if notes:
        notes = delete_notes(notes)
        print(Fore.GREEN + "Заметка удалена!" + Style.RESET_ALL)
    else:
        print("Нет заметок для удаления")
    return notes


def handle_search_note(notes):
    """
    Обработка поиска заметок.
    :param notes: Список заметок.
    """
    if notes:
        choice_search(notes)
    else:
        print("Нет заметок для поиска")


def menu(notes):
    """
    Основное меню программы.
    :param notes: Список заметок.
    """
    while True:
        # Вывод меню
        print(Fore.CYAN + "\nМеню действий:" + Style.RESET_ALL)
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы")

        # Получение выбора пользователя
        choice = input(Fore.YELLOW + "Ваш выбор: " + Style.RESET_ALL)

        # Обработка выбора пользователя
        if choice == '1':
            handle_create_note(notes)
        elif choice == '2':
            display_notes(notes)
        elif choice == '3':
            handle_update_note(notes)
        elif choice == '4':
            notes = handle_delete_note(notes)
        elif choice == '5':
            handle_search_note(notes)
        elif choice == '6':
            print(Fore.GREEN + "Программа завершена. Спасибо за использование!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Неверный выбор. Пожалуйста, выберите действие из списка." + Style.RESET_ALL)


def main():
    """
    Основная функция для запуска программы.
    """
    print(Fore.CYAN + "Добро пожаловать в 'Менеджер заметок'!" + Style.RESET_ALL)
    notes = []  # Инициализация списка заметок
    menu(notes)  # Запуск меню


# Точка входа в программу
if __name__ == "__main__":
    main()