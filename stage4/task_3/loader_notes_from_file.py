# Загружает заметки из текстового файла и возвращает их в виде списка словарей
def load_notes_from_file(filename):
    notes = []  # Список для хранения загруженных заметок
    try:
        # Попытка открыть файл в режиме чтения ('r')
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
                    print("Обнаружена неполная заметка. Пропускаем.")
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
                    else:
                        print(
                            f"Некорректная строка в заметке: '{line}'. "
                            f"Пропускаем."
                        )
                        continue

                notes.append(note)  # Добавляем заметку в список

    except FileNotFoundError:
        # Если файл не найден, создаем его и выводим сообщение
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                pass
            print(f"Файл '{filename}' не найден. Создан новый файл.")
            return notes  # Возвращаем пустой список, так как файл пустой
        except IOError as e:
            # Обработка ошибок при создании файла
            print(f"Ошибка при создании файла '{filename}': {e}")
            return notes  # Возвращаем пустой список, так как файл не создан
    except IOError as e:
        # Обработка других ошибок ввода-вывода
        print(f"Ошибка при чтении файла '{filename}': {e}")
    except Exception as e:
        # Обработка всех остальных ошибок
        print(f"Произошла ошибка при загрузке файла: {e}")

    return notes  # Возвращаем список заметок

# Точка входа
if __name__ == "__main__":
    # Загрузка заметок из файла
    notes = load_notes_from_file('notes.txt')
    for note in notes:
        print(note)
