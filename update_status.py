# vars
note = {
        'status': {
                    "var": ["В работе"],
                    "comment": ["Статус заметки"]
                    },
        }

# works
print("Введите новый статус заметки:")
note['status']['var'] = input("Новый статус: ")

print(f'Текущий статус заметки: {note['status']['var']}')
