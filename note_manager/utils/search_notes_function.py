# Импортируем необходимые модули
from colorama import Fore, Style, init

# Инициализация colorama
init(autoreset=True)


# Функция для форматирования и отображения найденных заметок
def format_notes(notes):
    if not notes:
        print(Fore.RED + "Заметки, соответствующие запросу, не найдены."
              + Style.RESET_ALL)
        return

    for i, note in enumerate(notes, start=1):
        print(Fore.YELLOW + "-" * 20 + Style.RESET_ALL)
        print(Style.BRIGHT + Fore.GREEN + f"Заметка №{i}:" + Style.RESET_ALL)
        print(
            Fore.LIGHTWHITE_EX + "Имя пользователя: " + Style.BRIGHT +
            Fore.WHITE + note["username"]
        )
        for j, title in enumerate(note["titles"], start=1):
            print(
                Fore.LIGHTWHITE_EX + f'- Заголовок заметки № {j}: '
                                     f'{Style.BRIGHT + Fore.WHITE}{title}'
            )
        print(
            Fore.LIGHTWHITE_EX + "Описание заметки: " + Style.BRIGHT +
            Fore.WHITE + note["content"]
        )
        print(
            Fore.LIGHTWHITE_EX + "Статус заметки: " + Style.BRIGHT +
            Fore.WHITE + note["status"]
        )
        print(
            Fore.LIGHTWHITE_EX + 'Дата создания заметки: ' + Style.BRIGHT +
            Fore.WHITE + note['created_date']
        )
        print(
            Fore.LIGHTWHITE_EX + 'Дедлайн: ' + Style.BRIGHT +
            Fore.WHITE + note['issue_date']
        )


# Функция для поиска заметок
def search_notes(notes, keywords=None, status=None):
    if not notes:
        print(Fore.RED + "Список заметок пуст." + Style.RESET_ALL)
        return []

    keyword_results = []
    status_results = []

    # Поиск по ключевым словам
    if keywords:
        keywords_list = keywords.lower().split(",")
        for note in notes:
            if any(
                keyword.strip() in str(value).lower()
                for keyword in keywords_list
                for value in [note["username"]] +
                note["titles"] + [note["content"]]
            ):
                keyword_results.append(note)

    # Поиск по статусу
    if status:
        for note in notes:
            if note["status"].lower() == status.lower():
                status_results.append(note)

    # Объединение результатов и исключение дубликатов
    combined_results = {
        id(note): note for note in keyword_results + status_results
    }.values()

    return list(combined_results)


def choice_search(notes):
    print(
        Fore.YELLOW + "Подсказка: Вы можете вводить несколько ключевых слов, \
разделяя их запятой." + Style.RESET_ALL
    )

    # Ввод ключевых слов
    keyword = input(Fore.YELLOW + "Введите ключевые слова для поиска \
(или оставьте пустым): " + Style.RESET_ALL).strip()

    # Ввод статуса
    status = input(Fore.YELLOW + "Введите статус для поиска \
(или оставьте пустым): " + Style.RESET_ALL).strip()

    # Проверка на пустые вводы
    if not keyword and not status:
        print(Fore.RED + "Не введены критерии поиска. Пожалуйста, \
введите хотя бы одно условие." + Style.RESET_ALL)
        return

    # Поиск заметок с учетом обоих параметров
    found_notes = search_notes(
        notes, keywords=keyword if keyword else None,
        status=status if status else None
    )
    format_notes(found_notes)

    print(Fore.YELLOW + "-" * 20 + Style.RESET_ALL)


# Основная функция для запуска программы
def main():
    print(
        Fore.CYAN + "Добро пожаловать в 'Менеджер заметок'!" +
        Style.RESET_ALL
    )
    choice_search(notes)


# Точка входа
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
