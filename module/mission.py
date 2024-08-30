from datetime import datetime, timedelta


class Mission:
    def __init__(self, name, duration, amount, start_time):
        self.name = name
        self.duration = duration
        self.amount = amount
        self.start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        self.end_time = self.start_time + timedelta(hours=self.duration)
        self.assigned_soldiers = []  # Changed to a list to handle multiple soldiers
        self.is_completed = False

    def assign_soldiers(self, soldiers):
        self.assigned_soldiers.extend(soldiers)  # Assign multiple soldiers
        for soldier in soldiers:
            soldier.task_history.append(self)

    def complete_mission(self):
        self.is_completed = True
        self.assigned_soldiers = []

    def get_assign_soldiers(self):
        return self.assigned_soldiers
