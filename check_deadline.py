# Импортируем необходимые модули для работы с датами
from datetime import datetime

# Создали словарь для хранения данных заметки
note = {}


# Функция проверки дедлайна
def check_deadline():
    # Получаем текущую дату
    current_date = datetime.now()
    print(f"Текущая дата: {current_date.strftime('%d-%m-%Y')}")

    while True:
        # Запрашиваем у пользователя дату дедлайна
        note["issue_date"] = input("Введите дату дедлайна \
в формате 'ДД-ММ-ГГГГ', например 25-12-2025): ")

        try:
            # Преобразуем строку из словаря в объект datetime
            dedline = datetime.strptime(note["issue_date"], "%d-%m-%Y")

            # Вычисляем разницу между текущей датой и дедлайном
            deadline_date = (dedline - current_date).days

            # Проверяем, истёк ли дедлайн
            if deadline_date < 0:
                print(f"Внимание! Дедлайн истёк \
{abs(deadline_date)} дня(ей) назад.")
            elif deadline_date == 0:
                print("Дедлайн сегодня!")
            else:
                print(f"До дедлайна осталось {deadline_date} дня(ей).")
            break  # Выход из цикла, если дата введена корректно

        except ValueError:
            print("Некорректный формат даты. Пожалуйста, \
используйте формат 'ДД-ММ-ГГГГ', например 25-12-2025.")


# Запускаем проверку дедлайна
check_deadline()
