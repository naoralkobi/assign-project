from module.mission import Mission
from module.soldier import Soldier
import csv
import io
from datetime import timedelta


class Company:
    def __init__(self, soldier_file, mission_file):
        self.soldiers = self.load_soldiers(soldier_file)
        self.missions = self.load_missions(mission_file)

    def load_soldiers(self, file_obj):
        soldiers = []
        # Decode the file contents and wrap it in a StringIO object to treat it as a text stream
        file_obj = io.TextIOWrapper(file_obj, encoding='utf-8')
        csv_reader = csv.DictReader(file_obj)
        for row in csv_reader:
            soldier = Soldier(
                soldier_id=row['soldier_id'],
                name=row['name'],
                department=row['department'],
                class_number=int(row['class_number']),
                phone_number=row['phone_number']
            )
            soldiers.append(soldier)
        return soldiers

    def load_missions(self, file_obj):
        missions = []
        # Decode the file contents and wrap it in a StringIO object to treat it as a text stream
        file_obj = io.TextIOWrapper(file_obj, encoding='utf-8')
        csv_reader = csv.DictReader(file_obj)
        for row in csv_reader:
            mission = Mission(
                mission_id=row['mission_id'],
                name=row['name'],
                duration=int(row['duration']),
                amount=int(row['amount']),
                start_time=row['start_time']
            )
            missions.append(mission)
        return missions

    def assign_tasks(self):
        for mission in self.missions:
            available_soldiers = []
            for soldier in self.soldiers:
                if soldier.task_history:
                    last_task = soldier.get_last_task()
                    # Check if the soldier's last task ended at least 2 * mission.duration hours before the new task starts
                    if last_task.end_time + timedelta(hours=2 * mission.duration) <= mission.start_time:
                        available_soldiers.append(soldier)
                else:
                    # Soldier has no task history, so they are available
                    available_soldiers.append(soldier)

            if available_soldiers:
                chosen_soldiers = available_soldiers[:mission.amount]
                mission.assign_soldiers(chosen_soldiers)
                assigned_names = ', '.join([s.name for s in chosen_soldiers])
                print(f"Assigned {assigned_names} to {mission.name}")
            else:
                print(f"No available soldier for mission: {mission.name}")

    def complete_mission(self, mission_id):
        mission = next((m for m in self.missions if m.mission_id == mission_id), None)
        if mission:
            mission.complete_mission()
            print(f"Mission {mission.name} completed.")
        else:
            print(f"Mission ID {mission_id} not found.")
