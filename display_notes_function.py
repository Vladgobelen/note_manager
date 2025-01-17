# Импортируем необходимые модули
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)


# Функция для отображения всех заметок
def display_notes(notes):
    total_notes = len(notes)
    print(Fore.CYAN + "\nСписок заметок:" + Style.RESET_ALL)

    # Проверка на наличие заметок
    if total_notes == 0:
        print(Fore.RED + "У вас нет сохранённых заметок." + Style.RESET_ALL)
        return

    # Переменная для отслеживания текущей страницы
    current_page = 0
    notes_per_page = 5

    while current_page * notes_per_page < total_notes:
        start_index = current_page * notes_per_page
        end_index = start_index + notes_per_page
        for i, note in enumerate(
                notes[start_index:end_index],
                start=start_index + 1
        ):  # Перебор заметок на текущей странице
            print(Fore.YELLOW + "-"*20 + Style.RESET_ALL)
            print(Style.BRIGHT + Fore.GREEN + f"Заметка №{i}\
:" + Style.RESET_ALL)
            print(Fore.LIGHTWHITE_EX + "Имя пользователя\
: " + Style.BRIGHT + Fore.WHITE + note["username"])
            # Перебор заголовков заметки
            for j, title in enumerate(note["titles"], start=1):
                print(Fore.LIGHTWHITE_EX + f'- Заголовок № {j}\
: {Style.BRIGHT + Fore.WHITE}{title}')
            print(Fore.LIGHTWHITE_EX + "Описание\
:" + Style.BRIGHT + Fore.WHITE + note["content"])
            print(Fore.LIGHTWHITE_EX + "Статус\
: " + Style.BRIGHT + Fore.WHITE + note["status"])
            print(Fore.LIGHTWHITE_EX + 'Дата создания\
: ' + Style.BRIGHT + Fore.WHITE + note['created_date'])
            print(Fore.LIGHTWHITE_EX + 'Дедлайн\
: ' + Style.BRIGHT + Fore.WHITE + note['issue_date'])

        # Увеличиваем номер страницы
        current_page += 1

        # Если есть еще заметки, предлагаем пользователю продолжить
        if current_page * notes_per_page < total_notes:
            input(Fore.YELLOW + "Нажмите Enter, чтобы \
продолжить..." + Style.RESET_ALL)


# Основная функция для запуска программы
def main():
    print(Fore.CYAN + "Добро пожаловать в 'Менеджер \
заметок'!" + Style.RESET_ALL)
    display_notes(notes)  # Вывод всех заметок после завершения ввода
    print(Fore.YELLOW + "-"*20 + Style.RESET_ALL)


# точка входа
if __name__ == "__main__":
    # Список для хранения всех заметок
    notes = [
        {
            'username': 'Алексей',
            'titles': ['Список покупок'],
            'content': 'Купить продукты на неделю',
            'status': 'новая',
            'created_date': '12-01-2025',
            'issue_date': '13-02-2025'
        },
        {
            'username': 'Мария',
            'titles': ['Учеба', 'Спорт'],
            'content': 'Подготовиться к экзамену',
            'status': 'в процессе',
            'created_date': '01-01-2025',
            'issue_date': '25-06-2025'
        },
        {
            'username': 'Иван',
            'titles': ['Работа', 'Проект'],
            'content': 'Завершить проект к концу месяца',
            'status': 'новая',
            'created_date': '10-01-2025',
            'issue_date': '30-01-2025'
        },
        {
            'username': 'Елена',
            'titles': ['Здоровье'],
            'content': 'Записаться к врачу',
            'status': 'в процессе',
            'created_date': '15-01-2025',
            'issue_date': '20-01-2025'
        },
        {
            'username': 'Сергей',
            'titles': ['Путешествие'],
            'content': 'Спланировать отпуск',
            'status': 'новая',
            'created_date': '20-01-2025',
            'issue_date': '15-03-2025'
        },
        {
            'username': 'Анна',
            'titles': ['Книги'],
            'content': 'Прочитать новые книги',
            'status': 'в процессе',
            'created_date': '25-01-2025',
            'issue_date': '01-04-2025'
        }
    ]
    # Запуск основной функции
    main()
