# vars
note = {
        'status': {
                    "var": ["в процессе"],
                    "comment": ["Статус заметки"],
                    "check": ["в процессе", "выполнено", "отложено"]
                    },
        }
# defs


def get_var(key, link):
    if link:
        for i, values in enumerate(note[key]['var']):
            print(f'{note[key]['comment'][i]}: {values}')
    else:
        for i, values in enumerate(note[key]['var']):
            print(f'{note[key]['comment'][0]}: {values}')


def set_key(key, value, mod, message):
    if note[key]['check']:
        if check_key(key, message):
            note[key][value][mod] = message
            print(f"{note[key]['comment'][0]} изменен на: {message}")
        else:
            print(f'"{message}" является недопустимым словом. Выберите из: ')
            print(*note[key]['check'], sep="\n")


def check_key(key, words):
    for word in note[key]['check']:
        if word in words:
            return 1


# works
get_var("status", None)
index = 0
while True:
    status = note['status']['comment'][0]
    var = input(f'Укажите новый {status} или введите ничего для завершения: ')
    if var == "":
        get_var("status", None)
        break
    else:
        set_key('status', 'var', 0, var)
