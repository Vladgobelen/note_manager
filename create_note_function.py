from datetime import datetime as dt
from copy import deepcopy
# vars
notes = []
note = {
        'username': {
                    "var": [""],
                    "comment": 'имя пользователя',
                    "check": ["all"]
                    },
        'title': {
                    "var": [],
                    "comment": "заголовок заметки",
                    "check": ["all"]
                    },
        'content': {
                    "var": [""],
                    "comment": "описание заметки",
                    "check": ["all"]
                    },
        'status': {
                    "var": [""],
                    "comment": "статус заметки",
                    "check": ["в процессе", "выполнено", "отложено"]
                    },
        'created_date': {
                        "var": [""],
                        "comment": "Дата создания заметки(ДД-ММ-ГГГГ)",
                        "check": ["all"]
                        },
        'issue_date': {
                        "var": [""],
                        "comment": "Дата истечения заметки(ДД-ММ-ГГГГ)",
                        "check": ["all"]
                        }
        }
# defs


def check_key(my_dict, key, var, words):  # does the word exist
    for word in my_dict[key][var]:
        if word in words:
            return 1


def comment(my_dict, var):  # returns the comment of the note
    return my_dict[var]['comment']


def check_exit(key):  # checking the correct input(exit)
    word = input(comment(note, key) + ": ")
    if check_key(note, key, "check", word):
        return word
    else:
        print(f'"{word}" является недопустимым словом. Выберите из: \n')
        print(*note[key]['check'], sep="\n")
        return ""


def input_status():  # checking the status entry
    print("\nВведите статус заметки: ", end="")
    print(*note["status"]['check'], sep=", ")
    while True:
        word = check_exit("status")
        if word != "":
            break
    return word


def input_title():  # checking the title entry
    title = []
    while True:
        print("Введите заголовок или нажмите энтер для завершения: ", end="")
        word = input()
        if word == "":
            break
        else:
            title.append(word)
    return title


def input_date(key):  # checking the date entry
    format = "%d-%m-%Y"
    while True:
        created_date = input(comment(note, key) + ': ')
        try:
            bool(dt.strptime(created_date, format))
            return created_date
        except ValueError:
            print("Неправильный формат даты (ДД-ММ-ГГГ), попробуйте еще раз: ")


def input_today():  # checking the date entry
    format = "%d-%m-%Y"
    return dt.now().strftime(format)


def create_note():  # Creating a note
    while True:
        name = input('Введите ' + comment(note, "username") + ': ')
        notes[len(notes)-1]['username']['var'].clear()
        notes[len(notes)-1]['username']['var'].append(name)
        title = input_title()
        notes[len(notes)-1]['title']['var'] = title
        content = input('Введите ' + comment(note, "content") + ': ')
        notes[len(notes)-1]['content']['var'].clear()
        notes[len(notes)-1]['content']['var'].append(content)
        status = input_status()
        notes[len(notes)-1]['status']['var'].clear()
        notes[len(notes)-1]['status']['var'].append(status)
        notes[len(notes)-1]['created_date']['var'].clear()
        notes[len(notes)-1]['created_date']['var'].append(input_today())
        create = input_date('issue_date')
        notes[len(notes)-1]['issue_date']['var'].clear()
        notes[len(notes)-1]['issue_date']['var'].append(create)
        break
    return notes[len(notes)-1]


# work
notes.append(deepcopy(note))
print(create_note())
