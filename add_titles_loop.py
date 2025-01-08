# vars
note = {
        'username': {
                    "var": [],
                    "comment": ['Имя пользователя']
                    },
        'title1': {
                    "var": [],
                    "comment": ["Заголовок заметки"]
                    },
        'content': {
                    "var": [],
                    "comment": ["Описание заметки"]
                    },
        'status': {
                    "var": [],
                    "comment": ["Статус заметки"]
                    },
        'created_date': {
                        "var": [],
                        "comment": ["Дата создания заметки(ДД-ММ-ГГГГ)"]
                        },
        'issue_date': {
                        "var": [],
                        "comment": ["Дата истечения заметки(ДД-ММ-ГГГГ)"]
                        }
        }
# working
print("Введите следущие данные(для завершения введите пустую строку): \n")
for key in note:
    while True:
        temp_text = input(f'{note[key]['comment'][0]}: ')
        if temp_text == "":
            note[key]['var'] = list(set(note[key]['var']))
            break
        else:
            note[key]['var'].append(temp_text)

print("\n")
for key in note:
    for var in note[key]["var"]:
        if key == "created_date" or key == "issue_date":
            value = "-".join(var.split(sep="-")[:2])
            try:
                print(f'{note[key]["comment"][0]}: ', value)
            except Exception as e:
                print(e)
        else:
            try:
                print(f'{note[key]["comment"][0]}: ', var)
            except Exception as e:
                print(e)
