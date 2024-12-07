def write_read_file(
    list_tasks: list = None, task_manager_class: object = None, choices: str = "w"
) -> None:
    """
    Функция для записи или чтения данных о задачах в/из файла "tasks.csv".

    Аргументы:
        tasks (list, optional): Список задач.
        choices (str, optional): Режим работы с файлом.

    - Если 'choices' равно "w", функция записывает
        информацию о задачах  в файл "tasks.csv"
        (id, name, description, category, period_execution,priority,status).

    - Если 'choices' отличается от "w", функция читает строки из файла,
        обрабатывает их и добавляет задачи в объект.

    Исключения:
        - При чтении файла: если строка в файле не соответствует
          ожидаемому формату, выводится сообщение "Нет записи".

    """

    print(list_tasks)
    # Открывает файл "tasks.csv" с указанным режимом (чтение или запись)
    with open("tasks.csv", choices, encoding="utf-8") as file:
        if choices == "w":
            for task in list_tasks:

                # Форматирует данные задачи в строку CSV и записываем в файл
                file.write(
                    f"{task.id},{task.name},{task.description},"
                    f"{task.category},{task.period_execution},"
                    f"{task.priority},{task.status}\n"
                )
        else:

            # Если режим чтения ("r"), пытается прочитать задачи из файла
            try:
                tasks_loaded = []
                for line in file:
                    # Разделят строку файла на атрибуты задачи по разделителю ","
                    (
                        id,
                        name,
                        description,
                        category,
                        period_execution,
                        priority,
                        status,
                    ) = line.strip().split(",")

                    # Добавляем задачу в менеджер задач
                    tasks_loaded.append(
                        {
                            # "id": id,
                            "name": name,
                            "description": description,
                            "category": category,
                            "period_execution": period_execution,
                            "priority": priority,
                            "status": status,
                        }
                    )
                return tasks_loaded

            except ValueError:
                # Если файл пуст или данные некорректны, выводит сообщение
                print("Пустой файл")
