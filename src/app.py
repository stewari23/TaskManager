from flask import Flask, jsonify, redirect, render_template, request, url_for, session

app = Flask(
    __name__,
    static_folder='../static',
    template_folder='../templates'
)

app.secret_key = 'a_random_secret_key_12345'

# In-memory data storage
projects = []

@app.route('/')
def index():
    return render_template('landing.html', logged_in=session.get('logged_in', False))

@app.route('/about')
def about():
    return render_template('about.html', logged_in=session.get('logged_in', False))

@app.route('/contact')
def contact():
    return render_template('contact.html', logged_in=session.get('logged_in', False))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulate login (replace with real authentication logic)
        session['logged_in'] = True
        return redirect(url_for('dashboard'))
    return render_template('login.html', logged_in=session.get('logged_in', False))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return jsonify(message='Signup successful. Please log in.')
    return render_template('signup.html', logged_in=session.get('logged_in', False))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if not session.get('logged_in', False):
        return redirect(url_for('login'))

    if request.method == 'POST':
        project_name = request.form.get('project_name')
        if project_name:
            projects.append({"name": project_name, "tasks": []})
            return jsonify(message=f"Project '{project_name}' added successfully!")
    return render_template('dashboard.html', projects=projects, logged_in=session.get('logged_in', False))



@app.route('/projects/<project_name>', methods=['GET', 'POST'])
def project_view(project_name):
    # Check if user is logged in
    if not session.get('logged_in', False):
        return redirect(url_for('login'))

    # Find the project
    project = next((p for p in projects if p['name'].lower() == project_name.lower()), None)
    if not project:
        return redirect(url_for('dashboard'))

    # Handle task addition
    if request.method == 'POST':
        task = {
            "name": request.form.get('name'),
            "priority": request.form.get('priority'),
            "due_date": request.form.get('due_date'),
            "status": request.form.get('status'),
            "assigned_to": request.form.get('assigned_to')
        }
        if not task["name"]:
            return jsonify(error="Task name is required."), 400

        project['tasks'].append(task)
        return jsonify(message=f"Task '{task['name']}' added successfully!")

    # Render the project page
    return render_template('project.html', project=project, logged_in=session.get('logged_in', False))


@app.route('/delete_task/<project_name>', methods=['POST'])
def delete_task(project_name):
    project = next((p for p in projects if p['name'] == project_name), None)
    if not project:
        return jsonify(message=f"Project '{project_name}' not found.")

    task_name = request.form.get('name')
    project['tasks'] = [task for task in project['tasks'] if task['name'] != task_name]
    return jsonify(message=f"Task '{task_name}' deleted successfully!")

@app.route('/delete_project/<project_name>', methods=['POST'])
def delete_project(project_name):
    global projects
    projects = [p for p in projects if p['name'] != project_name]
    return jsonify(message=f"Project '{project_name}' deleted successfully!")

@app.route('/edit_task/<project_name>', methods=['POST'])
def edit_task(project_name):
    project = next((p for p in projects if p['name'] == project_name), None)
    if not project:
        return jsonify(message=f"Project '{project_name}' not found.")

    original_name = request.form.get('original_name')
    task = next((t for t in project['tasks'] if t['name'] == original_name), None)
    if not task:
        return jsonify(message=f"Task '{original_name}' not found.")

    # Update task details
    task['name'] = request.form.get('name', task['name'])
    task['priority'] = request.form.get('priority', task['priority'])
    task['due_date'] = request.form.get('due_date', task['due_date'])
    task['status'] = request.form.get('status', task['status'])
    task['assigned_to'] = request.form.get('assigned_to', task['assigned_to'])

    return jsonify(message=f"Task '{original_name}' updated successfully!")


if __name__ == "__main__":
    app.run(debug=True)
