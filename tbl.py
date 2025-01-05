# variables
result = {}
t_note = {
        'username': 'Имя пользователя: ',
        'title1': "Заголовок заметки 1: ",
        'title2': "Заголовок заметки 2: ",
        'title3': "Заголовок заметки 3: ",
        'content': "Описание заметки: ",
        'status': "Статус заметки: ",
        'created_date': "Дата создания заметки: ",
        'issue_date': "Дата истечения заметки: ",
        }
# working

for key, value in t_note.items():
    result[key] = input(value)

for key, value in result.items():
    print(t_note[key], value)
