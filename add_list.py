import datetime

# functions


def add_titles(number):  # Adding three headers
    for i in range(1, number+1):
        title.append(input(f'Заголовок заметки номер {i}: '))


def read_titles():  # Reading three headers
    for i in range(1, len(title)+1):  # headers output
        print(f'Заголовок заметки номер {i}: {title[i-1]}')


# variables
username = input('Имя пользователя: ')
title = []
add_titles(3)
content = input('Описание заметки: ')
status = input('Статус заметки: ')
created_date = datetime.datetime.now().strftime('%d-%m-%Y')
issue_date = input('Дата истечения заметки (день-месяц-год): ')

# working
print('\nИмя пользователя:', username)
read_titles()
print('Описание заметки:', content)
print('Статус заметки:', status)
print('Дата создания заметки:', "-".join(created_date.split(sep="-")[:2]))
print('Дата истечения заметки:', "-".join(issue_date.split(sep="-")[:2]))
