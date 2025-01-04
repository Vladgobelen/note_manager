import datetime

# variables
username = input('Имя пользователя: ')
title = []
for i in range(1, 4):  # Adding three headers
    title.append(input(f'Заголовок заметки номер {i}: '))
content = input('Описание заметки: ')
status = input('Статус заметки: ')
created_date = datetime.datetime.now().strftime('%d-%m-%Y')
issue_date = input('Дата истечения заметки (день-месяц-год): ')

# working
print('\nИмя пользователя:', username)
for i in range(1, 4):  # headers output
    print(f'Заголовок заметки номер {i}: {title[i-1]}')
print('Описание заметки:', content)
print('Статус заметки:', status)
print(created_date)
print('Дата создания заметки:', "-".join(created_date.split(sep="-")[:2]))
print('Дата истечения заметки:', "-".join(issue_date.split(sep="-")[:2]))
