# from cla import ConsoleInterface
# from task_manager import TaskManager


class App:

    def __init__(self, interface_cls, task_manager_cls):

        self.interface = interface_cls()
        self.task_manager = task_manager_cls()
        # self.interface = ConsoleInterface()
        # self.task_manager = TaskManager()

    def run(self) -> None:
        while True:
            self.interface.display_menu()
            choice = self.interface.get_user_choice()
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.delete_task()
            elif choice == "3":
                self.search_task()
            elif choice == "4":
                self.show_tasks()
            elif choice == "0":
                self.interface.display_message("Программа завершена.")
                break
            else:
                self.interface.display_message("Неверный выбор, попробуйте снова.")

    def add_task(self) -> None:
        task_data = self.interface.get_task_input()
        self.task_manager.add_task(**task_data)
        self.interface.display_message("Задача успешно добавлена!")

    def delete_task(self) -> None:
        task_id = input("Введите ID задачи для удаления: ")
        self.task_manager.delete_task(int(task_id))
        self.interface.display_message("Задача успешно удалена!")

    def search_task(self) -> None:
        criteria = {"status": input("Введите статус задачи для поиска: ")}
        tasks = self.task_manager.search_tasks(criteria)
        self.interface.display_tasks(tasks)

    def show_tasks(self) -> None:
        tasks = self.task_manager.get_tasks()
        self.interface.display_tasks(tasks)
