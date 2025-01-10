import datetime
from datetime import datetime as dt
# vars
note = {
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


def input_value():
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


# works
print("Введите следущие данные(для завершения введите пустую строку): \n")
input_value()

print("\n")
while True:
    try:
        get_var("issue_date", None, 1)
        if get_date(note['issue_date']['var'][0]) == 1:
            break
    except ValueError:
        note['issue_date']['var'] = []
        print("Введите правилно дату: ДД-ММ-ГГ")
        input_value()
