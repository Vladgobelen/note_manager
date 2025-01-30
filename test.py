import note_manager as nt
notes = []
print("Добро пожаловать в 'Менеджер заметок'!")
while True:
    if nt.interface.menu(notes) == '6':
        break
