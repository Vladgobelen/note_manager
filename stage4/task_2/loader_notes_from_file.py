# Загружает заметки из текстового файла и возвращает их в виде списка словарей.
def load_notes_from_file(filename):
    notes = []  # Список для хранения загруженных заметок
    try:
        # Открываем файл в режиме чтения ('r')
        with open(filename, 'r', encoding='utf-8') as file:
            # Читаем содержимое файла и убираем лишние пробелы
            content = file.read().strip()

            if not content:  # Проверка на пустой файл
                print(f"Файл '{filename}' пустой.")
                return notes

            # Разбиваем содержимое на заметки по разделителю '---'
            raw_notes = content.split('---')
            for raw_note in raw_notes:
                # Разбиваем заметку на строки
                lines = raw_note.strip().split('\n')
                if len(lines) < 6:  # Проверяем, что заметка полная
                    continue

                # Создаем словарь для каждой заметки
                note = {}
                for line in lines:
                    # Разделяем строку на ключ и значение
                    # Разделяем только на первый ': '
                    key_value = line.split(': ', 1)
                    # Убедимся, что ключ и значение существуют
                    if len(key_value) == 2:
                        key, value = key_value
                        if key == 'titles':
                            # Если ключ 'titles', разбиваем значение на список
                            note[key] = value.split(', ')
                        else:
                            note[key] = value

                notes.append(note)  # Добавляем заметку в список
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка при загрузке файла: {e}")

    return notes  # Возвращаем список заметок


# Точка входа
if __name__ == "__main__":
    # Загрузка заметок из файла
    notes = load_notes_from_file('notes.txt')
    for note in notes:
        print(note)
