from abstract import AbstractInterface
from validator_input import checing_date, get_choice_category, get_validator_input


class ConsoleInterface(AbstractInterface):
    def display_menu(self) -> None:
        print("МЕНЮ:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Найти задачу")
        print("4. Показать все задачи")
        print("5. Обновить задачу")
        print("0. Выход")

    # def get_user_input(self, prompt: str) -> str:
    #     pass

    def get_user_choice(self) -> str:
        return input("Выберите действие: ")

    def display_tasks(self, tasks: list) -> None:
        if not tasks:
            self.display_message("Список задач пуст.")
            return
        self.display_message("ЗАДАЧИ:")
        for task in tasks:
            self.display_message(task)

    def display_message(self, message: str) -> None:
        print(message)

    def get_user_input(self) -> dict:

        name = get_validator_input(
            "Введите название задачи: ",
            lambda x: len(x.strip()) > 0,
            f"{'-' * 40}\nОШИБКА! Поле 'name' не может быть пустым\n{'-' * 40}",
        )
        description = get_validator_input(
            "Введите описание задачи: ",
            lambda x: len(x.strip()) > 0,
            f"{'-' * 40}\nОШИБКА! Поле 'name' не может быть пустым\n{'-' * 40}",
        )
        # Выбрать категорию через валидатор
        category = get_choice_category()

        # Срок выполнения задачи
        print("Введите срок выполнения задачи (YYYY-MM-DD): ")
        period_execution = checing_date()

        priority = input("Введите приоритет задачи (Низкий/Средний/Высокий): ")
        return {
            "name": name,
            "description": description,
            "category": category,
            "period_execution": period_execution,
            "priority": priority,
        }
