from copy import deepcopy
# vars
notes = []
note = {
        'username': {
                    "var": ["Имя"],
                    "comment": 'имя пользователя',
                    "check": ["all"]
                    },
        'title': {
                    "var": ['Заголовок'],
                    "comment": "заголовок заметки",
                    "check": ["all"]
                    },
        'content': {
                    "var": ["Описание"],
                    "comment": "описание заметки",
                    "check": ["all"]
                    },
        'status': {
                    "var": ["статус"],
                    "comment": "статус заметки",
                    "check": ["в процессе", "выполнено", "отложено"]
                    },
        'created_date': {
                        "var": ["Сегодня"],
                        "comment": "Дата создания заметки(ДД-ММ-ГГГГ)",
                        "check": ["all"]
                        },
        'issue_date': {
                        "var": ["Завтра"],
                        "comment": "Дата истечения заметки(ДД-ММ-ГГГГ)",
                        "check": ["all"]
                        }
        }
# defs


def is_notes():  # does the note exist
    if len(notes) >= 1 and notes[0]['username']['var'][0] != '':
        return 1


def show_print():  # information about notes
    if is_notes():
        print(print_notes())
        return 1
    else:
        print("\nНет ни одной заметки\n")


def print_notes():  # summary of the notes
    result = "\nЗаметки: \n\n"
    i = 1
    for note in notes:
        result = result + f'Заметка номер {i}' + '\n'
        result = result + "\nИмя: " + note['username']['var'][0] + "\n"
        result = result + "Заголовки: "
        i = 0
        for titles in note['title']['var']:
            result = result + str(i+1) + ") " + titles + " "
            i += 1
        result = result + "\nОписание: "
        result = result + note['content']['var'][0] + "\n"
        result = result + "Статус: " + note['status']['var'][0] + "\n"
        frase = "Дата создания: " + note['created_date']['var'][0] + "\n"
        result = result + frase
        frase = "Дата истечения: " + note['issue_date']['var'][0] + "\n"
        result = result + frase
        i += 1
    return result


notes.append(deepcopy(note))
show_print()
