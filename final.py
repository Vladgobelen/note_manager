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
print('\n' + note['username'])
print(note['title'][0])
print(note['title'][1])
print(note['title'][2])
print(note['content'])
print(note['status'])
print(note['created_date'])
print(note['issue_date'])
