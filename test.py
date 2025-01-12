import datetime
from datetime import datetime as dt
from copy import deepcopy
# vars
notes = []
delete_list = "Выберите: удалить, создать заметку, сменить статус или выйти"
note = {
        'delete': {
                    "var": [""],
                    "comment": delete_list,
                    "check": ["удалить", "создать", "выйти", "сменить статус"],
                    "check_del": ["все заметки", "по заголовку", "по имени"]
                    },
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


def is_notes():  # does the note exist
    if len(notes) >= 1 and notes[0]['username']['var'][0] != '':
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


def check_exit(key):  # checking the correct input(exit)
    word = input(comment(note, key) + ": ")
    if check_key(note, key, "check", word):
        return word
    else:
        print(f'"{word}" является недопустимым словом. Выберите из: \n')
        print(*note[key]['check'], sep="\n")
        return ""


def del_note():  # deleting notes
    while True:
        if show_print():
            print("Напишите, что удалять: ", end="")
            print(*note['delete']['check_del'], sep=", ", end=": ")
            word = input()
            if check_key(notes[len(notes)-1], "delete", "check_del", word):
                if word == "все заметки":
                    notes.clear()
                elif word == "по заголовку":
                    del_by('title', input("Введите заголовок: "))
                elif word == "по имени":
                    del_by('username', input("Введите имя: "))
                break
            else:
                print(f'"{word}" это недопустимое слово. Выберите из: \n')
                print(*notes[len(notes)-1]["delete"]['check_del'], sep="\n")
        else:
            break


def get_current_day(my_date):  # get days from a date
    return my_date.days


def check_date(first_date, second_date):  # subtract dates from each other
    return get_current_day((first_date)-(second_date))


def get_date(my_date):  # comparing dates
    today = datetime.datetime.now()
    check_day = dt.strptime(my_date, '%d-%m-%Y')
    return check_date(today, check_day)


def deadline(my_dict, my_date):  # deadline check
    count = get_date(my_dict['issue_date']['var'][0])
    if count > 0:
        result = "Дедлайн прошел " + str(count) + " дней назад"
        return result
    elif count == 0:
        result = "Дедлайн сегодня"
        return result
    elif count < 0:
        result = "Дедлайн пойдет через " + str(abs(count)) + " дней"
        return result


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
        if note['issue_date']['var'][0] != "":
            result = result + deadline(note, note['issue_date']['var'][0])
            result = result + '\n\n'
        i += 1
    return result


def show_print():  # information about notes
    if is_notes():
        print(print_notes())
        return 1
    else:
        print("\nНет ни одной заметки\n")


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


def input_status():  # checking the status entry
    print("\nВведите статус заметки: ", end="")
    print(*note["status"]['check'], sep=", ")
    while True:
        word = check_exit("status")
        if word != "":
            break
    return word


def input_date(key):  # checking the date entry
    format = "%d-%m-%Y"
    while True:
        created_date = input(comment(note, key) + ': ')
        try:
            bool(dt.strptime(created_date, format))
            return created_date
        except ValueError:
            print("Неправильный формат даты (ДД-ММ-ГГГ), попробуйте еще раз: ")


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
        create = input_date('created_date')
        notes[len(notes)-1]['created_date']['var'].clear()
        notes[len(notes)-1]['created_date']['var'].append(create)
        create = input_date('issue_date')
        notes[len(notes)-1]['issue_date']['var'].clear()
        notes[len(notes)-1]['issue_date']['var'].append(create)
        break


def change_status():
    status = int(input("Введите номер изменяемой заметки: "))
    notes[status-1]['status']['var'].clear()
    notes[status-1]['status']['var'].append(input_status())


def work():  # The main code
    show_print()
    while True:
        exit_word = check_exit("delete")
        if exit_word == "выйти":
            break
        elif exit_word == "удалить":
            if is_notes():
                del_note()
            else:
                print("Нечего удалять")
        elif exit_word == "создать":
            notes.append(deepcopy(note))
            create_note()
        elif exit_word == "сменить статус":
            if is_notes():
                change_status()
            else:
                print("Нет заметок для изменения статуса")
        show_print()


# works
print('Добро пожаловать в "Менеджер заметок"!\n')

work()
print("\n")
