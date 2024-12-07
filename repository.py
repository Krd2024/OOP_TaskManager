from abstract import AbstractRepository
from write_read import write_read_file


class RepositoryManager(AbstractRepository):
    # def __init__(self):
    # tasks_list = []

    def load_tasks(self):
        return write_read_file(choices="r")

    def save_tasks(self, tasks: list) -> None:
        write_read_file(list_tasks=tasks, choices="w")

    def delete_task(self, task_id: int) -> None:
        pass
