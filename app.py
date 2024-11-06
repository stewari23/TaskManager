from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Database connection helper function
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route
@app.route('/')
def index():
    return render_template('landing.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Login route
@app.route('/login')
def login():
    return render_template('login.html')

# Signup route with form handling
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the username or email already exists
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? OR email = ?', (username, email)).fetchone()
        
        if user:
            flash('Username or email already exists. Please use a different one.')
            conn.close()
            return redirect(url_for('signup'))
        
        # Insert new user into the database with hashed password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                     (username, email, hashed_password))
        conn.commit()
        conn.close()
        
        flash('Account created successfully! Please log in.')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
