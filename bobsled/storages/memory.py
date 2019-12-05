from ..base import Status


class InMemoryStorage:
    def __init__(self):
        self.runs = []
        self.tasks = {}

    async def connect(self):
        pass

    async def add_run(self, run):
        self.runs.append(run)

    async def save_run(self, run):
        # run is modified in place
        pass

    async def get_run(self, run_id):
        run = [r for r in self.runs if r.uuid == run_id]
        if run:
            return run[0]

    async def get_runs(self, *, status=None, task_name=None, latest=None):
        runs = [r for r in self.runs]
        if isinstance(status, Status):
            runs = [r for r in runs if r.status == status]
        elif isinstance(status, list):
            runs = [r for r in runs if r.status in status]
        elif status:
            raise ValueError("status must be Status or list")
        if task_name:
            runs = [r for r in runs if r.task == task_name]
        if latest:
            # runs are in order, so just grab the tail
            runs = runs[-latest:]
        return runs

    def get_tasks(self):
        return list(self.tasks.values())

    def get_task(self, name):
        return self.tasks[name]

    def set_tasks(self, tasks):
        self.tasks = {task.name: task for task in tasks}
