# variables
note = {
        'username': '',
        'title': [],
        'content': '',
        'status': '',
        'created_date': '',
        'issue_date': '',
        }
title = []
note['username'] = input('Имя пользователя: ')
note['title'].append(input('Заголовок заметки 1: '))
note['title'].append(input('Заголовок заметки 2: '))
note['title'].append(input('Заголовок заметки 3: '))
note['content'] = input('Описание заметки: ')
note['status'] = input('Статус заметки: ')
note['created_date'] = input('Дата создания заметки(дд-мм-гггг): ')
note['issue_date'] = input('Дата истечения заметки (дд-мм-гггг): ')

# working
print('\nИмя пользователя:', note['username'])
print('Заголовок заметки 1:', note['title'][0])
print('Заголовок заметки 2:', note['title'][1])
print('Заголовок заметки 3:', note['title'][2])
print('Описание заметки:', note['content'])
print('Статус заметки:', note['status'])
print('Дата создания заметки: ', end="")
print("-".join(note['created_date'].split(sep="-")[:2]))
print('Дата истечения заметки: ', end="")
print("-".join(note['issue_date'].split(sep="-")[:2]))
