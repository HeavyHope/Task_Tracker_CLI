# TASK TRACKER CLI

## Description:

* This program is designed to remind you of your tasks, their status and time of addition.
* The program can change the task status, update the description, delete and add a new one.
* Json file will be created automatically

## how to start?

* python main.py ==your code==
## list of commands and how to work with them:

1. Add new task

```python
python main.py add task_name
```

  You must enter the add command and then provide a description of the new task

2. Delete task

```python
python main.py delete id_task
```

You must enter the command delete and then task ID

3. View your task list

```python
python main.py list
```

But you can also pass an argument and sort the list of tasks by their status

```python
python main.py list todo
```

4. Update your task description or status

```python
python main.py update task_id new_description
```

To change the description of a task, enter update then the ID of the task whose description you want to change and then enter a new description of the task

```python
python main.py update task_id new_status
```

You can also change the status setting; to do this, instead of a description, enter a new status
