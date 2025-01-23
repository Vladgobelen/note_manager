# Сохраняет список заметок в текстовый файл
def save_notes_to_file(notes, filename):
    try:
        # Открываем файл в режиме записи ('w'), перезаписывая его содержимое
        with open(filename, 'w', encoding='utf-8') as file:
            for note in notes:
                # Записываем имя пользователя
                file.write(f"Имя пользователя: {note['username']}\n")

                # Записываем все заголовки заметки
                for title in note["titles"]:
                    file.write(f"Заголовок: {title}\n")

                # Записываем описание, статус, дату создания и дедлайн
                file.write(f"Описание: {note['content']}\n")
                file.write(f"Статус: {note['status']}\n")
                file.write(f"Дата создания: {note['created_date']}\n")
                file.write(f"Дедлайн: {note['issue_date']}\n")

                # Разделитель между заметками
                file.write("---\n")
    except PermissionError:
        # Обработка ошибки доступа
        print(f"Ошибка доступа: "
              f"у вас нет разрешения на запись в файл {filename}.")
    except Exception as e:
        # Обработка всех остальных ошибок
        print(f"Ошибка при работе с файлом {filename}: {e}")
        # Корректно завершаем выполнение программы
        return


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
        }
    ]

    # Вызываем функцию для сохранения заметок в файл
    save_notes_to_file(notes, 'notes.txt')