from flask import Flask, render_template, request, redirect, url_for, session

from db_handler import get_soldiers_list
from module.company import Company
import os
from utils import verify_user, verify_user_is_mm_commander
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Generates a random 16-byte key

# Paths for CSV files
SOLDIER_FILE = 'soldiers.csv'
MISSION_FILE = 'missions.csv'

# Global variable for Company object
company = None


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    user_id = request.form['user_id']
    password = request.form['password']

    user = verify_user(user_id, password)
    if user:
        session['user'] = user
        return redirect(url_for('menu'))
    else:
        error_message = 'Invalid user ID or password. Please try again.'
        return render_template('login.html', error=error_message)


@app.route('/logout')
def logout():
    session.pop('user', None)  # Clear the user session
    return redirect(url_for('index'))


@app.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('index'))
    user = session['user']
    return render_template('profile.html', user=user)


@app.route('/presence')
def presence():
    if 'user' not in session:
        return redirect(url_for('index'))
    user = session['user']
    if not verify_user_is_mm_commander(user):
        return render_template('menu.html', user=user, role=user.get('role'))
    soldiers = get_soldiers_list(department_condition=user.get('department'))
    return render_template('presence.html', user=user, soldiers=soldiers)


@app.route('/submit_presence', methods=['POST'])
def submit_presence():
    if 'user' not in session:
        return redirect(url_for('index'))
    user = session['user']

    presence_data = {}
    for key, value in request.form.items():
        soldier_id, hour = key.split('_')
        if soldier_id not in presence_data:
            presence_data[soldier_id] = {}
        presence_data[soldier_id][hour] = value

    save_presence_data(presence_data)

    return redirect(url_for('menu'))


def save_presence_data(presence_data):
    # Implement the logic to save presence data to the database
    # Example: iterate over presence_data and update the corresponding rows in the database
    pass


@app.route('/requests')
def requests():
    return "Requests page."


@app.route('/tasks')
def tasks():
    return "Tasks page."


@app.route('/assignment')
def assignment():
    return "Assignment page."


@app.route('/training')
def training():
    return "Training page."


@app.route('/qualifications')
def qualifications():
    return "Qualifications page."


@app.route('/upload', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        # Get the uploaded soldier and mission files
        soldier_file = request.files['soldier_file']
        mission_file = request.files['mission_file']

        # Pass the file objects directly to the Company constructor
        global company
        company = Company(soldier_file, mission_file)
        return redirect(url_for('assign_tasks'))

    return render_template('upload.html')


@app.route('/menu')
def menu():
    if 'user' not in session:
        return redirect(url_for('index'))
    user = session['user']
    role = user.get('role')
    return render_template('menu.html', user=user, role=role)


@app.route('/assign', methods=['GET', 'POST'])
def assign_tasks():
    if company is None:
        return redirect(url_for('upload_files'))

    if request.method == 'POST':
        company.assign_tasks()
        return redirect(url_for('view_tasks'))

    return render_template('tasks.html')


@app.route('/tasks')
def view_tasks():
    if company is None:
        return redirect(url_for('upload_files'))

    tasks = []
    for mission in company.missions:
        for soldier in mission.assigned_soldiers:  # Corrected variable name 'soldier'
            tasks.append({
                'mission_name': mission.name,
                'soldier': soldier.name,  # Changed key from 'soldiers' to 'soldier'
                'start_time': mission.start_time.strftime('%Y-%m-%d %H:%M:%S'),
                'end_time': mission.end_time.strftime('%Y-%m-%d %H:%M:%S')
            })

    return render_template('tasks.html', tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5454)
