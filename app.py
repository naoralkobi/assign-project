from flask import Flask, render_template, request, redirect, url_for, flash
from module.company import Company
import os
from utils import verify_user
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

    if verify_user(user_id, password):
        return redirect(url_for('menu'))
    else:
        error_message = 'Invalid user ID or password. Please try again.'
        return render_template('login.html', error=error_message)


@app.route('/profile')
def profile():
    return "Profile page."


@app.route('/present')
def present():
    return "Present page."


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
    return render_template('menu.html')


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
