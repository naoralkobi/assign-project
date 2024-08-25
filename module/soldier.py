class Soldier:
    def __init__(self, soldier_id, name, department, class_number, phone_number):
        self.soldier_id = soldier_id
        self.name = name
        self.department = department
        self.class_num = class_number
        self.phone_number = phone_number
        self.task_history = []

    def __str__(self):
        return f'{self.soldier_id},{self.name},{self.department},{self.class_num},{self.phone_number}'

    def __repr__(self):
        return f'Soldier(id={self.soldier_id}, name={self.name}, department={self.department})'

    def add_task(self, task):
        self.task_history.append(task)

    def get_last_task(self):
        return self.task_history[-1]

    def get_task_history(self):
        return self.task_history
