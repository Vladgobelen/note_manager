import json


# Сохраняет список заметок в текстовый файл
def save_notes_json(notes, filename):
    try:
        # Открываем файл в режиме записи ('w'), перезаписывая его содержимое
        with open(filename, 'w', encoding='utf-8') as file:
            # Записываем список формате json с кириллицей, с отступами
            json.dump(notes, file, ensure_ascii=False, indent=4)
    except PermissionError:
        # Обработка ошибки доступа
        print(f"Ошибка доступа: "
              f"у вас нет разрешения на запись в файл {filename}.")
    except Exception as e:
        # Обработка всех остальных ошибок
        print(f"Ошибка при работе с файлом {filename}: {e}")


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
    save_notes_json(notes, 'notes.json')
