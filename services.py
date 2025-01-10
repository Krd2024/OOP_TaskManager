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
            elif choice == "5":
                self.update_task()
            elif choice == "0":
                self.interface.display_message("Программа завершена.")
                break
            else:
                self.interface.display_message("Неверный выбор, попробуйте снова.")

    def check_id(self, task_id):
        tasks = self.task_manager.get_tasks()

        task = next((t for t in tasks if t.id == task_id), None)
        # task = [t for t in tasks if t.id == task_id]
        print(task, "< - task", "|", task_id, "< - task_id")

        return task
        # if not task:
        #     print(f"Задача с ID {task_id} не найдена.")
        #     return

    def add_task(self) -> None:
        task_data = self.interface.get_user_input()
        results = self.task_manager.add_task(**task_data)
        self.interface.display_message(results)

    def delete_task(self) -> None:
        task_id = input("Введите ID задачи для удаления: ")
        results = self.task_manager.delete_task(int(task_id))
        self.interface.display_message(results)

    def search_task(self) -> None:
        criteria = {"status": input("Введите статус задачи для поиска: ")}
        tasks = self.task_manager.search_tasks(criteria)
        self.interface.display_tasks(tasks)

    def update_task(self) -> None:
        task_id = input("Введите ID задачи для обновления: ")
        task = self.check_id(int(task_id))
        print(task, "< - task update")
        if task is None:
            self.interface.display_message(f"Задача с ID {task_id} не найдена.")
        else:
            new_task_data = self.interface.get_user_input()
            self.task_manager.update_task(task, new_task_data)

    def show_tasks(self) -> None:
        tasks = self.task_manager.get_tasks()
        self.interface.display_tasks(tasks)
