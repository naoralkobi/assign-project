from db_handler import get_soldiers_list


def verify_user(user_id, password):
    soldiers = get_soldiers_list()
    for soldier in soldiers:
        if user_id == soldier.get('soldier_id') and password == soldier.get('password'):
            return soldier
    return None


def verify_user_is_mm_commander(user):
    return user.get('role') == 'mm_commander'
