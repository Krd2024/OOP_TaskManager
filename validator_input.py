import datetime
from data import DICT_CATEGORY


def get_validator_input(promt: str, validate: callable, err_message: str):
    while True:
        value = input(promt)
        if validate(value):
            return " ".join(value.split())
        print(err_message)


def get_choice_category():
    while True:
        print("Выберите категорию:\n1. Работа\n2. Личное\n3. Обучение")
        choice = input("Выбор: ")
        if choice in DICT_CATEGORY:
            return DICT_CATEGORY[choice]
        continue


def checing_day(year, month, day):
    print(year, month, day)
    print(type(year), type(month), type(day))
    """
    Проверяет, является ли введённая комбинация месяца, дня и года корректной.

    - Определяет количество дней в каждом месяце с учётом високосного года.
    - Для февраля (месяц 2) устанавливает 29 дней, если год високосный.
    - Проверяет, входит ли значение дня в допустимый диапазон для указанного месяца.

    Возвращает True, если комбинация валидна, иначе False
    """

    dict_days_in_month = {
        "1": 31,
        "2": 28,
        "3": 31,
        "4": 30,
        "5": 31,
        "6": 30,
        "7": 31,
        "8": 31,
        "9": 30,
        "10": 31,
        "11": 30,
        "12": 31,
    }
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        dict_days_in_month["2"] = 29

    print(day in list(range(1, dict_days_in_month[month] + 1)))
    return day in list(range(1, dict_days_in_month[month] + 1))


def get_year():
    while True:
        # Запрашивает ввод года у пользователя, удаляет все пробелы
        year = input("Введите год: ").replace(" ", "")
        # Если год является числом, то проверяется, что он не меньше 2024
        if year.isdigit():
            # Получить текущий год
            current_year = datetime.datetime.now().year
            print(current_year, " - ", year)
            # Если год меньше текущего, выводится сообщение об ошибке
            if int(year) < current_year:
                print(f"{'-' * 40}\nОШИБКА! Ушли те времена\n{'-' * 40}")
                continue
        else:
            print(
                f"{'-' * 40}\nОШИБКА! Нужно вводить цифры.Попробуйте ещё раз\n{'-' * 40}"
            )
            continue
        return year


def get_month():
    while True:

        # Получить месяц
        month = input("Введите месяц: ").replace(" ", "")
        if month.isdigit():
            # Проверяет, что месяц находится в допустимом диапазоне от 1 до 12
            if int(month) < 1 or int(month) > 12:
                print(
                    f"{'-' * 40}\nnОШИБКА! Этот месяц не отсюда. Попробуйте ещё раз.\n{'-' * 40}"
                )
                continue
        return month


def get_day():
    while True:
        day = input("Введите день: ").replace(" ", "")
        if day.isdigit():
            return day
        continue


def checing_date():
    year = get_year()
    month = get_month()
    while True:
        day = get_day()
        checing = checing_day(int(year), month, int(day))
        if checing:
            break
        continue
    return f"{year}-{month}-{day}"
