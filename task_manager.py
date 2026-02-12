class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{status}] #{self.id}: {self.description}"
    
class TaskManager:  
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self._tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        if(not self._tasks):
            return "No tasks available."
        return self._tasks

    def complete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                return task
        return None

    def get_pending_tasks(self):
        return [task for task in self._tasks if not task.completed]

    def get_completed_tasks(self):
        return [task for task in self._tasks if task.completed]

    def __str__(self):
        return "\n".join(str(task) for task in self._tasks)