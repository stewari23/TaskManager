from flask import Flask, flash, jsonify, redirect, render_template, request, url_for



app = Flask(
    __name__,
    static_folder='../static',  # Points to static directory in src
    template_folder='../templates'  # Points to templates directory in src
)

app.secret_key = 'a_random_secret_key_12345'

tasks = []



@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Just redirect to the dashboard on form submission
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle the signup logic here
        username = request.form.get('username')
        password = request.form.get('password')
        # Add your logic to store the user in the database or validation

        # Redirect to the login page with a success message
        flash('Signup successful. Please log in.')
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        task = {
            "name": request.form.get('name'),
            "priority": request.form.get('priority'),
            "due_date": request.form.get('due_date'),
            "status": request.form.get('status'),
            "assigned_to": request.form.get('assigned_to')
        }
        tasks.append(task)
        return jsonify({"message": "Task added successfully", "tasks": tasks})
    return render_template('dashboard.html', tasks=tasks)

@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_name = request.form.get('name')
    global tasks
    tasks = [task for task in tasks if task['name'] != task_name]
    return jsonify({"message": "Task deleted successfully", "tasks": tasks})

if __name__ == "__main__":
    app.run(debug=True)
