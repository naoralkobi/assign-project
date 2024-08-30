from db_handler import get_soldiers_list


def verify_user(user_id, password):
    soldiers = get_soldiers_list(columns=["soldier_id", "password"])
    for soldier in soldiers:
        if user_id == soldier.get('soldier_id') and password == soldier.get('password'):
            return True
    return False
