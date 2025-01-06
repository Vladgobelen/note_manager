# variables
note = {
        'username': {
                    "var": [],
                    "comment": ['Имя пользователя']
                    },
        'title1': {
                    "var": [],
                    "comment": [
                                "Заголовок заметки 1",
                                "Заголовок заметки 2",
                                "Заголовок заметки 3"
                                ]
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
print("Введите следущие данные: \n")
for key in note:
    for comment in note[key]["comment"]:
        note[key]['var'].append(input(f'{comment}: '))

print("\n")
for key in note:
    for i in range(0, len(note[key]["comment"])):
        print(f'{note[key]["comment"][i]}: ', note[key]["var"][i])
