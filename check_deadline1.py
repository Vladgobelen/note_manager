import datetime
from datetime import datetime as dt
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


def get_var(key, link, end, n_index):  # Universal obtaining of variable values
    end_text = ""
    if end:
        end_text = "сохранено как"
    else:
        end_text = "изменено на"
    if link:
        for i, values in enumerate(notes[n_index][key]['var']):
            if key == "issue_date" or key == "created_date":
                format_date = "-".join(values.split(sep="-")[:2])
                print(f'{notes[n_index][key]['comment'][i]} {n_index} {end_text}: {format_date}')
            else:
                print(f'{notes[n_index][key]['comment'][i]} {n_index} {end_text}: {values}')
    else:
        for i, values in enumerate(notes[n_index][key]['var']):
            if key == "issue_date" or key == "created_date":
                format_date = "-".join(values.split(sep="-")[:2])
                print(f'{notes[n_index][key]['comment'][0]} {n_index} {end_text}: {format_date}')
            else:
                print(f'{notes[n_index][key]['comment'][0]} {n_index} {end_text}: {values}')


def set_key(key, value, mod, message, n_index):  # Variable entry
    if notes[n_index][key]['check']:
        if check_key(key, message) or notes[n_index][key]['check'][0] == "all":
            notes[n_index][key]['var'].append(message)
            if key == 'content':
                get_var(key, 1, None, n_index)
            else:
                get_var(key, None, None, n_index)
        else:
            print(f'"{message}" является недопустимым словом. Выберите из: ')
            print(*notes[n_index][key]['check'], sep="\n")


def check_key(key, words):  # Checking for a word match with the dictionary
    for word in notes[n_index][key]['check']:
        if word in words:
            return 1


def get_current_day(my_date):
    return my_date.strftime('%d')


def chek_date(first_date, second_date):
    return int(get_current_day(first_date))-int(get_current_day(second_date))


def get_date(issue_date):
    today = datetime.datetime.now()
    check_day = dt.strptime(issue_date, '%d-%m-%Y')
    if chek_date(today, check_day) > 0:
        print(f"Дедлайн прошел {chek_date(today, check_day)} дней назад")
    else:
        print(f"Дедлайн через {-1*int(chek_date(today, check_day))} дней")


# works
print("Введите следущие данные(для завершения введите пустую строку): \n")
n_index = 0
while True:
    notes.append(note)
    for key in note:
        index = 0
        while True:
            temp_text = input(f'{notes[n_index][key]['comment'][0]}: ')
            if temp_text == "":
                notes[n_index][key]['var'] = list(set(notes[n_index][key]['var']))
                notes[n_index][key]['var'].sort()
                print('112', notes)
                if key == "issue_date":
                    n_index += 1
                break
            else:
                set_key(key, 'var', index, temp_text, n_index)
                index += 1

print("\n")
n_index = 0
for i in range(0, len(notes)):
    for kye in notes[i]:
        n_index = 0
        if key == 'content':
            get_var(key, 1, 1, n_index)
        else:
            if key == "issue_date":
                get_var(key, None, 1, n_index)
                get_date(notes[n_index][key]['var'][0])
            else:
                get_var(key, None, 1, n_index)
