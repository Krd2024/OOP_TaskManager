from abstract import AbstractInterface


class ConsoleInterface(AbstractInterface):
    def display_menu(self) -> None:
        print("МЕНЮ:")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Найти задачу")
        print("4. Показать все задачи")
        print("0. Выход")

    def get_user_input(self, prompt: str) -> str:
        pass

    def get_user_choice(self) -> str:
        return input("Выберите действие: ")

    def display_tasks(self, tasks) -> None:
        if not tasks:
            print("Список задач пуст.")
            return
        print("\nЗАДАЧИ:")
        for task in tasks:
            print(task)

    def display_message(self, message: str) -> None:
        print(message)

    def get_task_input(self) -> dict:
        name = input("Введите название задачи: ")
        description = input("Введите описание задачи: ")
        category = input("Введите категорию задачи: ")
        period_execution = input("Введите срок выполнения задачи (YYYY-MM-DD): ")
        priority = input("Введите приоритет задачи (Низкий/Средний/Высокий): ")
        return {
            "name": name,
            "description": description,
            "category": category,
            "period_execution": period_execution,
            "priority": priority,
        }
