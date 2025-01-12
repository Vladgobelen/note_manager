from datetime import datetime as dt
# vars
note = {
        'update_note': {
                        "var": [""],
                        "comment": 'Введите которое поле менять',
                        "check": [
                                    "имя пользователя",
                                    "заголовок",
                                    "описание",
                                    "статус",
                                    "дата создания",
                                    "дата истечения"
                                ],
                        'check_list': {
                                        "имя пользователя": "username",
                                        "заголовок": "title",
                                        "описание": "content",
                                        "статус": "status",
                                        "дата создания": "created_date",
                                        "дата истечения": "issue_date"
                                        }
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


def check_key(my_dict, key, var, words):  # does the word exist
    for word in my_dict[key][var]:
        if word in words:
            return 1


def comment(my_dict, var):  # returns the comment of the note
    return my_dict[var]['comment']


def check_exit(key):  # checking the correct input(exit)
    word = input(comment(note, key) + ": ")
    if check_key(note, key, "check", word.lower()):
        return word
    else:
        print(f'"{word}" является недопустимым словом. Выберите из: \n')
        print(*note[key]['check'], sep="\n")
        return ""


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


def update_note(my_note):
    while True:
        word = check_exit("update_note")
        if word != "":
            if word.lower() == "имя пользователя":
                name = input('Введите ' + comment(my_note, "username") + ': ')
                my_note['username']['var'].clear()
                my_note['username']['var'].append(name)
                break
            elif word.lower() == "заголовок":
                title = input_title()
                my_note['title']['var'] = title
                break
            elif word.lower() == "описание":
                print("Введите ", end="")
                content = input(comment(my_note, "content") + ': ')
                my_note['content']['var'].clear()
                my_note['content']['var'].append(content)
                break
            elif word.lower() == "статус":
                status = input_status()
                my_note['status']['var'] = status
                break
            elif word.lower() == "дата создания":
                create = input_date('issue_date')
                my_note['created_date']['var'].clear()
                my_note['created_date']['var'].append(create)
                break
            elif word.lower() == "дата истечения":
                issue = input_date('issue_date')
                my_note['issue_date']['var'].clear()
                my_note['issue_date']['var'].append(issue)
                break


print(note)
update_note(note)
print(note)
