import json

class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{status}] #{self.id}: {self.description}"
    
class TaskManager:  
    
    FILE_NAME = "tasks.json"

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        self.save_tasks()
        return task

    def list_tasks(self):
        if(not self._tasks):
            return "No tasks available."
        self.load_tasks()
        return self._tasks

    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                self.save_tasks()
                return task
        return None
    
    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                self.save_tasks()
                return task
        return None

    def get_pending_tasks(self):
        return [task for task in self._tasks if not task.completed]

    def get_completed_tasks(self):
        return [task for task in self._tasks if task.completed]

    def __str__(self):
        return "\n".join(str(task) for task in self._tasks)
    
    def save_tasks(self):
        with open(self.FILE_NAME, "w") as f:
            json.dump([task.__dict__ for task in self._tasks], f)

    def load_tasks(self):
        try:
            with open(self.FILE_NAME, "r") as f:
                tasks_data = json.load(f)
                self._tasks = [Task(**data) for data in tasks_data]
                if self._tasks:
                    self._next_id = max(task.id for task in self._tasks) + 1
                else:
                    self._next_id = 1

        except FileNotFoundError:
            pass