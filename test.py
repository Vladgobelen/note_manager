import datetime
from datetime import datetime as dt
from copy import deepcopy
# vars
notes = []
note = {
        'delete': {
                    "var": "",
                    "comment": "Выберите: удалить, создать заметку или выйти",
                    "check": ["удалить", "создать", "выйти"],
                    "check_del": ["все заметки", "по заголовку", "по имени"]
                    },
        'username': {
                    "var": ["Влад"],
                    "comment": 'Имя пользователя',
                    "check": ["all"]
                    },
        'title': {
                    "var": ["первый", "второй"],
                    "comment": ["Заголовок заметки"],
                    "check": ["all"]
                    },
        'content': {
                    "var": "Тестовая заметка",
                    "comment": "Описание заметки",
                    "check": ["all"]
                    },
        'status': {
                    "var": "",
                    "comment": ["Статус заметки"],
                    "check": ["в процессе", "выполнено", "отложено"]
                    },
        'created_date': {
                        "var": "",
                        "comment": ["Дата создания заметки(ДД-ММ-ГГГГ)"],
                        "check": ["all"]
                        },
        'issue_date': {
                        "var": "",
                        "comment": ["Дата истечения заметки(ДД-ММ-ГГГГ)"],
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


def check_exit():  # checking the correct input(exit)
    word = input(comment(note, "delete") + ": ")
    if check_key(notes[len(notes)-1], "delete", "check", word):
        return word
    else:
        print(f'"{word}" является недопустимым словом. Выберите из: \n')
        print(*notes[len(notes)-1]["delete"]['check'], sep="\n")
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
        i = 1
        for titles in note['title']['var']:
            result = result + str(i) + ") " + titles + " "
        result = result + "\nОписание: "
        result = result + note['content']['var'] + "\n"
        return result


def show_print():  # information about notes
    if is_notes():
        print(print_notes())
    else:
        print("Нет ни одной заметки\n")
        notes.append(deepcopy(note))


def work(need_break):  # The main code
    show_print()
    while need_break == "да":
        exit_word = check_exit()
        if (exit_word) == "выйти":
            break
        elif (exit_word) == "удалить":
            del_note()
        else:
            pass
        show_print()


# works
print('Добро пожаловать в "Менеджер заметок"!\n')
need_break = "да"
work(need_break)
print("\n")
show_print()
