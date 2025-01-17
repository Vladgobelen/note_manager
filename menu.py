# Импортируем необходимые модули
from colorama import Fore, Style, init
from create_note_function import create_note
from update_note_function import update_note
from display_notes_function import display_notes
from delete_note import delete_notes
from search_notes_function import choice_search

# Инициализация colorama
init(autoreset=True)

# Список для хранения всех заметок
#     {
#         'username': 'Алексей',
#         'titles': ['Список покупок'],
#         'content': 'Купить продукты на неделю',
#         'status': 'новая',
#         'created_date': '12-01-2025',
#         'issue_date': '13-02-2025'
#     },
#     {
#         'username': 'Мария',
#         'titles': ['Учеба', 'Спорт'],
#         'content': 'Подготовиться к экзамену',
#         'status': 'в процессе',
#         'created_date': '01-01-2025',
#         'issue_date': '25-06-2025'
#     }
# ]
 
 
# Функция для удаления заметки
# def delete_note():
#     display_notes(notes)
#     note_index = int(input(Fore.YELLOW + "Введите номер заметки для удаления: " + Style.RESET_ALL)) - 1
#     if 0 <= note_index < len(notes):
#         confirm = input(Fore.RED + "Вы уверены, что хотите удалить эту заметку? (да/нет): " + Style.RESET_ALL)
#         if confirm.lower() == 'да':
#             del notes[note_index]
#             print(Fore.GREEN + "Заметка удалена!" + Style.RESET_ALL)
#         else:
#             print(Fore.YELLOW + "Удаление отменено." + Style.RESET_ALL)
#     else:
#         print(Fore.RED + "Неверный номер заметки." + Style.RESET_ALL)
 
 
# Функция для отображения меню и обработки выбора пользователя


def choice_note(notes):
    check_size = len(notes)
    while True:
        try:
            my_note = int(input("Введите номер заметки, которую нужно изменить: "))
            if int(my_note) >= 1 and int(my_note) <= check_size:
                return int(my_note)-1
            else:
                print("Такой заметки не существует")
        except Exception:
            print("Введите номер заметки - число")


def menu(notes):
    while True:
        print(Fore.CYAN + "\nМеню действий:" + Style.RESET_ALL)
        print("1. Создать новую заметку")
        print("2. Показать все заметки")
        print("3. Обновить заметку")
        print("4. Удалить заметку")
        print("5. Найти заметки")
        print("6. Выйти из программы")
        choice = input(Fore.YELLOW + "Ваш выбор: " + Style.RESET_ALL)
 
        if choice == '1':
            notes.append(create_note())
        elif choice == '2':
            display_notes(notes)  # Вывод всех заметок
        elif choice == '3':
            if len(notes):
                update_note(notes[choice_note(notes)])
            else:
                print("Нет заметок для изменения")
        elif choice == '4':
            if len(notes):
                notes = delete_notes(notes)
            else:
                print("Нет заметок для удаление")
        elif choice == '5':
            if len(notes):
                choice_search(notes)
            else:
                print("Нет заметок для поиска")
        elif choice == '6':
            print(Fore.GREEN + "Программа завершена. \
Спасибо за использование!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Неверный выбор. Пожалуйста, \
выберите действие из списка." + Style.RESET_ALL)
 
 
# Основная функция для запуска программы
def main():
    print(
        Fore.CYAN + "Добро пожаловать в 'Менеджер заметок'!" +
        Style.RESET_ALL
    )
    menu(notes)
 
 
# точка входа
if __name__ == "__main__":
    # Запуск основной функции
    notes = []
    main()
