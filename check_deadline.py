import datetime
from datetime import datetime as dt
# vars
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


def get_var(key, link, end):  # Universal obtaining of variable values
    end_text = ""
    if end:
        end_text = "сохранено как"
    else:
        end_text = "изменено на"
    if link:
        for i, values in enumerate(note[key]['var']):
            print(f'{note[key]['comment'][i]} {end_text}: {values}')
    else:
        for i, values in enumerate(note[key]['var']):
            print(f'{note[key]['comment'][0]} {end_text}: {values}')


def set_key(key, value, mod, message):  # Variable entry with validation
    if note[key]['check']:
        if check_key(key, message) or note[key]['check'][0] == "all":
            note[key]['var'].append(message)
            if key == 'content':
                get_var(key, 1, None)
            else:
                get_var(key, None, None)
        else:
            print(f'"{message}" является недопустимым словом. Выберите из: ')
            print(*note[key]['check'], sep="\n")


def check_key(key, words):  # Checking for a word match with the dictionary
    for word in note[key]['check']:
        if word in words:
            return 1


def chek_date(issue_date):
    today = datetime.datetime.now()
    check_day = dt.strptime(issue_date, '%d-%m-%Y')
    diff = today - check_day
    if int(diff.days) > 0:
        print(f"Дедлайн прошел {int(diff.days)} дней назад")
    else:
        print(f"Дедлайн будет через {-1*int(diff.days)} дней")


# works
print("Введите следущие данные(для завершения введите пустую строку): \n")
for key in note:
    index = 0
    while True:
        temp_text = input(f'{note[key]['comment'][0]}: ')
        if temp_text == "":
            note[key]['var'] = list(set(note[key]['var']))
            note[key]['var'].sort()
            break
        else:
            set_key(key, 'var', index, temp_text)
            index += 1

print("\n")
for key in note:
    if key == 'content':
        get_var(key, 1, 1)
    else:
        if key == "issue_date":
            get_var(key, None, 1)
            chek_date(note[key]['var'][0])
        else:
            get_var(key, None, 1)
