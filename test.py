import datetime
from datetime import datetime as dt
from copy import deepcopy
# vars
notes = []
note = {
        'delete': {
                    "var": [],
                    "comment": "Выберите: удалить, создать заметку или выйти",
                    "check": ["удалить", "создать", "выйти"],
                    "check_del": ["все заметки", "по заголовку", "по имени"]
                    },
        'username': {
                    "var": [],
                    "comment": 'имя пользователя',
                    "check": ["all"]
                    },
        'title': {
                    "var": [],
                    "comment": "заголовок заметки",
                    "check": ["all"]
                    },
        'content': {
                    "var": [],
                    "comment": "описание заметки",
                    "check": ["all"]
                    },
        'status': {
                    "var": [],
                    "comment": "статус заметки",
                    "check": ["в процессе", "выполнено", "отложено"]
                    },
        'created_date': {
                        "var": [],
                        "comment": "Дата создания заметки(ДД-ММ-ГГГГ)",
                        "check": ["all"]
                        },
        'issue_date': {
                        "var": [],
                        "comment": "Дата истечения заметки(ДД-ММ-ГГГГ)",
                        "check": ["all"]
                        }
        }

# defs


def is_notes():  # does the note exist
    if len(notes) >= 1 and notes[0]['username']['var'] != "":
        return 1


def check_key(my_dict, key, var, words):  # does the word exist
    for word in my_dict[key][var]:
        if word in words:
            return 1


def comment(my_dict, var):  # returns the comment of the note
    return my_dict[var]['comment']


def del_by(key, del_word):  # deleting a note by parameter
    for i, del_note in enumerate(notes):
        for position, del_title in enumerate(notes[i][key]['var']):
            if del_word == del_title:
                del notes[i]
                print('\nЗаметка удалена')
                if len(notes) == 0:
                    notes.append(deepcopy(note))


def check_exit(key):  # checking the correct input(exit)
    word = input(comment(note, key) + ": ")
    if check_key(notes[len(notes)-1], key, "check", word):
        return word
    else:
        print(f'"{word}" является недопустимым словом. Выберите из: \n')
        print(*notes[len(notes)-1][key]['check'], sep="\n")
        return ""


def del_note():  # deleting notes
    while True:
        print(print_notes())
        print("Напишите, что удалять: ", end="")
        print(*note['delete']['check_del'], sep=", ", end=": ")
        word = input()
        if check_key(notes[len(notes)-1], "delete", "check_del", word):
            if word == "все заметки":
                notes.clear()
                notes.append(deepcopy(note))
            elif word == "по заголовку":
                del_by('title', input("Введите заголовок: "))
            elif word == "по имени":
                del_by('username', input("Введите имя: "))
            break
        else:
            print(f'"{word}" является недопустимым словом. Выберите из: \n')
            print(*notes[len(notes)-1]["delete"]['check_del'], sep="\n")


def print_notes():  # summary of the notes
    result = ""
    for note in notes:
        result = "\nЗаметки: \n"
        result = result + "\nИмя: " + note['username']['var'][0] + "\n"
        result = result + "Заголовки: "
        i = 0
        for titles in note['title']['var']:
            result = result + str(i+1) + ") " + titles + " "
            i += 1
        result = result + "\nОписание: "
        result = result + note['content']['var'][0] + "\n"
        return result


def show_print():  # information about notes
    if is_notes():
        print(print_notes())
    else:
        print("Нет ни одной заметки\n")
        notes.append(deepcopy(note))


def input_title():
    title = []
    while True:
        print("Введите заголовок или нажмите энтер для завершения: ", end="")
        word = input()
        if word == "":
            break
        else:
            title.append(word)
    return title


def input_status():
    print("\nВведите статус заметки: ", end="")
    print(*note["status"]['check'], sep=", ")
    while True:
        word = check_exit("status")
        if word != "":
            break
    return word


def input_date(key):
    format = "%d-%m-%Y"
    while True:
        created_date = input(comment(note, key) + ': ')
        try:
            bool(dt.strptime(created_date, format))
            return created_date
        except ValueError:
            print("Неправильный формат даты (ДД-ММ-ГГГ), попробуйте еще раз: ")


def create_note():
    while True:
        name = input('Введите ' + comment(note, "username") + ': ')
        notes[len(notes)-1]['username']['var'].append(name)
        title = input_title()
        notes[len(notes)-1]['title']['var'] = title
        content = input('Введите ' + comment(note, "content") + ': ')
        notes[len(notes)-1]['content']['var'].append(content)
        status = input_status()
        notes[len(notes)-1]['status']['var'].append(status)
        create = input_date('created_date')
        notes[len(notes)-1]['created_date']['var'].append(create)
        create = input_date('issue_date')
        notes[len(notes)-1]['issue_date']['var'].append(create)
        print(notes)
        break


def work(need_break):  # The main code
    show_print()
    while need_break == "да":
        exit_word = check_exit("delete")
        if exit_word == "выйти":
            break
        elif exit_word == "удалить":
            del_note()
        elif exit_word == "создать":
            create_note()
        show_print()


# works
print('Добро пожаловать в "Менеджер заметок"!\n')
need_break = "да"
work(need_break)
print("\n")
show_print()
