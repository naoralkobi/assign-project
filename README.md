```markdown
# Task Assignment Program

A Python-based task assignment program that assigns tasks to soldiers based on availability. The program allows users to upload CSV files for soldiers and missions and then assigns tasks accordingly. It also provides a web interface for managing and viewing assigned tasks.

## Features
- Upload CSV files for soldiers and missions.
- Automatically assign tasks to available soldiers based on their task history.
- View assigned tasks with start and end times via a web interface.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/naoralkobi/assign-project.git
   cd task-assignment-program
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application:**
   ```bash
   python app.py
   ```

   By default, the application runs on `http://127.0.0.1:5000/`.

## Usage

1. **Upload CSV Files:**
   - Go to `http://127.0.0.1:5000/upload` to upload the soldiers and missions CSV files.
   
2. **Assign Tasks:**
   - After uploading, click the "Assign Tasks" button to automatically assign tasks to soldiers.

3. **View Assigned Tasks:**
   - Visit `http://127.0.0.1:5000/tasks` to view the assigned tasks, along with the start and end times.

## Technologies Used

- Python 3.9
- Flask
- HTML/CSS
- CSV for data handling
