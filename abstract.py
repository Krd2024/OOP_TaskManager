from abc import ABC, abstractmethod


class AbstractInterface(ABC):
    @abstractmethod
    def display_menu(self) -> None:
        pass

    @abstractmethod
    def get_user_input(self, prompt: str) -> str:
        pass

    @abstractmethod
    def display_message(self, message: str) -> None:
        pass


# =================================================================


class AbstractTaskService(ABC):
    """Менеджер управления задачами"""

    @abstractmethod
    def add_task(self, task_data: dict) -> None:
        pass

    @abstractmethod
    def update_task(self, task_id: int, updates: dict) -> None:
        pass

    @abstractmethod
    def search_tasks(self, criteria: dict) -> list:
        pass

    @abstractmethod
    def delete_task(self, task_id: int) -> None:
        pass

    @abstractmethod
    def get_tasks(self) -> None:
        pass


# =================================================================


class AbstractRepository(ABC):
    @abstractmethod
    def load_tasks(self) -> list:
        pass

    @abstractmethod
    def save_tasks(self, tasks: list) -> None:
        pass

    @abstractmethod
    def delete_task(self, task_id: int) -> None:
        pass
