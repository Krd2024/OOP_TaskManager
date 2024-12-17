from typing import List, Dict
from abstract import AbstractTaskService
from models import Task
from repository import RepositoryManager


class TaskManager(AbstractTaskService):
    """Менеджер управления задачами"""

    tasks = []

    def __init__(self):

        # Объект менеджера репозитория
        self.repository = RepositoryManager()
        # Загружаем задачи из хранилища
        tasks_in_file = self.repository.load_tasks()
        # Создать объекты задач
        for task in tasks_in_file:
            self.add_task(**task)

    def add_task(self, **task_data: tuple) -> None:
        """
        Добавляет новую задачу в список задач и сохраняет её в репозитории.
        :param task_data: словарь с параметрами задачи.
        """
        try:
            task = Task(*task_data.values())

            self.tasks.append(task)
            self.repository.save_tasks(self.tasks)
        except Exception as e:
            return f"Ошибка: {e}"
        return f"Задача '{task.name}' успешно добавлена."

    def get_tasks(self) -> list:
        return self.tasks

    def update_task(self, task: object, updates: Dict) -> None:
        """
        Обновляет параметры существующей задачи.
        :param task_id: уникальный идентификатор задачи.
        :param updates: словарь с обновленными данными.
        """
        # task = next((t for t in self.tasks if t.id == task_id), None)
        # if not task:
        #     print(f"Задача с ID {task_id} не найдена.")
        #     return

        for key, value in updates.items():
            setattr(task, key, value)
        self.repository.save_tasks(self.tasks)
        print(f"Задача '{task.name}' успешно обновлена.")

    def search_tasks(self, criteria: Dict) -> List[Task]:
        """
        Выполняет поиск задач по заданным критериям.
        :param criteria: словарь с параметрами поиска (например, по ключевым словам или статусу).
        :return: список найденных задач.
        """

        found_tasks = [
            task
            for task in self.tasks
            if all(
                (
                    getattr(task, key, "").lower() == value.lower()
                    if isinstance(value, str)
                    else getattr(task, key) == value.lower()
                )
                for key, value in criteria.items()
            )
        ]
        return found_tasks
        if found_tasks:
            print("Найдены задачи:")
            for task in found_tasks:
                print(task)
        else:
            print("Задачи не найдены.")

    def delete_task(self, task_id: int) -> None:
        """
        Удаляет задачу по её идентификатору.
        :param task_id: уникальный идентификатор задачи.
        """
        task = next((t for t in self.tasks if t.id == task_id), None)
        if not task:
            return f"Задача с ID {task_id} не найдена."

        self.tasks.remove(task)
        self.repository.save_tasks(self.tasks)
        return f"Задача '{task.name}' успешно удалена."
