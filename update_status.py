# vars
note = {
        'status': {
                    "var": ["в процессе"],
                    "comment": ["Статус заметки"],
                    "check": ["в процессе", "выполнено", "отложено"]
                    },
        }
# defs


def get_var(key, link):  # Universal obtaining of variable values
    if link:
        for i, values in enumerate(note[key]['var']):
            print(f'{note[key]['comment'][i]}: {values}')
    else:
        for i, values in enumerate(note[key]['var']):
            print(f'{note[key]['comment'][0]}: {values}')


def set_key(key, value, mod, message):  # Variable entry with validation
    if note[key]['check']:
        if check_key(key, message):
            note[key][value][mod] = message
            print(f"{note[key]['comment'][0]} изменен на: {message}")
        else:
            print(f'"{message}" является недопустимым словом. Выберите из: ')
            print(*note[key]['check'], sep="\n")


def check_key(key, words):  # Checking for a word match with the dictionary
    for word in note[key]['check']:
        if word in words:
            return 1


# works
get_var("status", None)  # Getting the current status.
while True:  # Recording a new status
    status = note['status']['comment'][0]
    var = input(f'Укажите новый {status} или введите ничего для завершения: ')
    if var == "":  # Exiting the program
        get_var("status", None)
        break
    else:  # Status changed
        set_key('status', 'var', 0, var)
