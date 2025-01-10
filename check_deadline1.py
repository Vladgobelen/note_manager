import datetime
from datetime import datetime as dt
from copy import deepcopy
# vars
notes = []
note = {
        'username': {
                    "var": [],
                    "comment": ['Имя пользователя'],
                    "check": ["all"]
                    },
        'title1': {
                    "var": [],
                    "comment": ["Заголовок заметки"],
                    "check": ["all"]
                    },
        'content': {
                    "var": [],
                    "comment": [
                                "Описание заметки",
                                "Описание заметки",
                                ],
                    "check": ["all"]
                    },
        'status': {
                    "var": [],
                    "comment": ["Статус заметки"],
                    "check": ["в процессе", "выполнено", "отложено"]
                    },
        'created_date': {
                        "var": [],
                        "comment": ["Дата создания заметки(ДД-ММ-ГГГГ)"],
                        "check": ["all"]
                        },
        'issue_date': {
                        "var": [],
                        "comment": ["Дата истечения заметки(ДД-ММ-ГГГГ)"],
                        "check": ["all"]
                        }
        }

# defs


def get_var(key, link, end, note):  # Universal obtaining of variable values
    end_text = ""
    if end:
        end_text = "сохранено как"
    else:
        end_text = "изменено на"
    if link:
        for i, values in enumerate(note[key]['var']):
            if key == "issue_date" or key == "created_date":
                format_date = "-".join(values.split(sep="-")[:2])
                print(f'{note[key]['comment'][i]} {end_text}: {format_date}')
            else:
                print(f'{note[key]['comment'][i]} {end_text}: {values}')
    else:
        for i, values in enumerate(note[key]['var']):
            if key == "issue_date" or key == "created_date":
                format_date = "-".join(values.split(sep="-")[:2])
                print(f'{note[key]['comment'][0]} {end_text}: {format_date}')
            else:
                print(f'{note[key]['comment'][0]} {end_text}: {values}')


def set_key(key, value, mod, message, n_index):  # Variable entry
    if notes[n_index][key]['check']:
        if check_key(key, message) or notes[n_index][key]['check'][0] == "all":
            notes[n_index][key]['var'].append(message)
            if key == 'content':
                get_var(key, 1, None, notes[n_index])
            else:
                get_var(key, None, None, notes[n_index])
        else:
            print(f'"{message}" является недопустимым словом. Выберите из: ')
            print(*notes[n_index][key]['check'], sep="\n")


def check_key(key, words):  # Checking for a word match with the dictionary
    for word in notes[n_index][key]['check']:
        if word in words:
            return 1


def check_key(key, words):  # Checking for a word match with the dictionary
    for word in note[key]['check']:
        if word in words:
            return 1


def get_current_day(my_date):
    return my_date.days


def check_date(first_date, second_date):
    return get_current_day((first_date)-(second_date))


def get_date(my_date):
    today = datetime.datetime.now()
    check_day = dt.strptime(my_date, '%d-%m-%Y')
    if check_date(today, check_day) > 0:
        print(f"Дедлайн прошел {check_date(today, check_day)} дней назад")
        return 1
    else:
        print(f"Дедлайн через {-1*int(check_date(today, check_day))} дней")
        return 1


# works
print("Введите следущие данные(для завершения введите пустую строку): \n")
n_index = 0
need_break = "да"
while need_break == "да":
    notes.append(deepcopy(note))
    for key in note:
        index = 0
        while True:
            temp_text = input(f'{notes[n_index][key]['comment'][0]}: ')
            if temp_text == "":
                notes[n_index][key]['var'] = list(set(notes[n_index][key]['var']))
                notes[n_index][key]['var'].sort()
                if key == "issue_date":
                    need_break = input("Добавить еще одну заметку?(да нет)")
                    n_index += 1
                break
            else:
                set_key(key, 'var', index, temp_text, n_index)
                index += 1

print("\n")
for note in notes:
    for kye in note:
        if key == 'content':
            get_var(key, 1, 1, note)
        else:
            if key == "issue_date":
                get_var(key, None, 1, note)
                get_date(note[key]['var'][0])
            else:
                get_var(key, None, 1, note)
