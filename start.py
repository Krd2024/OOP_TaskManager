from services import App
from cla import ConsoleInterface
from task_manager import TaskManager

app = App(ConsoleInterface, TaskManager)
app.run()
