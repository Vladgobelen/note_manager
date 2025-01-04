import datetime

# variables
username = input('Имя пользователя: ')
title = input('Заголовок заметки: ')
content = input('Описание заметки: ')
status = input('Статус заметки: ')
created_date = datetime.datetime.now().strftime('%d-%m-%Y')
issue_date = input('Дата истечения заметки (день-год-месяц): ')

# working
print('Имя пользователя:', username)
print('Заголовок заметки:', title)
print('Описание заметки:', content)
print('Статус заметки:', status)
print(created_date)
print('Дата создания заметки:', "-".join(created_date.split(sep="-")[:2]))
print('Дата истечения заметки:', "-".join(issue_date.split(sep="-")[:2]))
