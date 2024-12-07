from abc import ABC, abstractmethod
from typing import List, Dict
from abstract import AbstractTaskService, AbstractRepository
from models import Task
from repository import RepositoryManager
from write_read import write_read_file


class TaskManager(AbstractTaskService):
    tasks = []

    def __init__(self):

        # Объект менеджера репозитория
        self.repository = RepositoryManager()
        tasks_in_file = self.repository.load_tasks()  # Загружаем задачи из хранилища

        for task in tasks_in_file:
            self.add_task(**task)

    def add_task(self, **task_data: tuple) -> None:
        """
        Добавляет новую задачу в список задач и сохраняет её в репозитории.
        :param task_data: словарь с параметрами задачи.
        """
        task = Task(*task_data.values())

        self.tasks.append(task)
        self.repository.save_tasks(self.tasks)

        print(f"Задача '{task.name}' успешно добавлена.")

    def get_tasks(self) -> list:
        return self.tasks

    def update_task(self, task_id: int, updates: Dict) -> None:
        """
        Обновляет параметры существующей задачи.
        :param task_id: уникальный идентификатор задачи.
        :param updates: словарь с обновленными данными.
        """
        task = next((t for t in self.tasks if t.id == task_id), None)
        if not task:
            print(f"Задача с ID {task_id} не найдена.")
            return

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
        if found_tasks:
            print("Найдены задачи:")
            for task in found_tasks:
                print(task)
        else:
            print("Задачи не найдены.")
        return found_tasks

    def delete_task(self, task_id: int) -> None:
        """
        Удаляет задачу по её идентификатору.
        :param task_id: уникальный идентификатор задачи.
        """
        task = next((t for t in self.tasks if t.id == task_id), None)
        if not task:
            print(f"Задача с ID {task_id} не найдена.")
            return

        self.tasks.remove(task)
        self.repository.save_tasks(self.tasks)
        print(f"Задача '{task.name}' успешно удалена.")


#
# print(TaskManager())
