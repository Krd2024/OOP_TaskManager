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
            # print(DICT_CATEGORY[choice])
            return DICT_CATEGORY[choice]
        continue
