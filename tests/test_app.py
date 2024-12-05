import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    """Test if the homepage loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Task Manager' in response.data


def test_about(client):
    """Test if the about page loads correctly."""
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About Task Manager' in response.data


def test_contact(client):
    """Test if the contact page loads correctly."""
    response = client.get('/contact')
    assert response.status_code == 200
    assert b'Contact Us' in response.data


def test_login(client):
    """Test if the login page loads correctly."""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login' in response.data


def test_login_post_success(client):
    """Test if POST to login works correctly and redirects to dashboard."""
    response = client.post('/login', data={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 302  
    assert response.location == '/dashboard'


def test_login_session(client):
    """Test if session is updated correctly after login."""
    client.post('/login', data={'username': 'testuser', 'password': 'testpass'})
    with client.session_transaction() as session:
        assert session.get('logged_in') is True


def test_signup(client):
    """Test if the signup page loads correctly."""
    response = client.get('/signup')
    assert response.status_code == 200
    assert b'Sign Up' in response.data


def test_signup_post_success(client):
    """Test if POST to signup returns success message."""
    response = client.post('/signup', data={'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 200
    assert b'Signup successful. Please log in.' in response.data


def test_signup_not_allowed_methods(client):
    """Test if unsupported methods on signup return 405."""
    response = client.delete('/signup') 
    assert response.status_code == 405


def test_dashboard(client):
    """Test if the dashboard page loads correctly."""
    user = {
        'username': 'testuser',
        'password': 'testpassword'
    }    
    client.post('/login', data=user) 
    response = client.get('/dashboard')
    assert response.status_code == 200
    assert b'Dashboard' in response.data


def test_add_project(client):
    """Test adding a new project."""
    client.post('/login')  # Log in the user
    response = client.post('/dashboard', data={'project_name': 'Test Project'})
    assert response.status_code == 200
    assert b"Project 'Test Project' added successfully!" in response.data


def test_add_task(client):
    """Test adding a new task to a project."""
    client.post('/login')  # Log in the user
    client.post('/dashboard', data={'project_name': 'Test Project'}) 
    response = client.post('/projects/Test Project', data={
        'name': 'Test Task',
        'priority': 'High',
        'due_date': '2024-12-31',
        'status': 'In Progress',
        'assigned_to': 'Test User'
    })
    assert response.status_code == 200
    assert b"Task 'Test Task' added successfully!" in response.data


def test_edit_task(client):
    """Test editing a task in a project."""
    client.post('/login')  
    client.post('/dashboard', data={'project_name': 'Test Project'})  
    client.post('/projects/Test Project', data={
        'name': 'Test Task',
        'priority': 'High',
        'due_date': '2024-12-31',
        'status': 'In Progress',
        'assigned_to': 'Test User'
    }) 

    response = client.post('/edit_task/Test Project', data={
        'original_name': 'Test Task',
        'name': 'Updated Task',
        'priority': 'Low',
        'due_date': '2025-01-01',
        'status': 'Completed',
        'assigned_to': 'Updated User'
    })
    assert response.status_code == 200
    assert b"Task 'Test Task' updated successfully!" in response.data


def test_delete_task(client):
    """Test deleting a task from a project."""
    client.post('/login')  
    client.post('/dashboard', data={'project_name': 'Test Project'})  
    client.post('/projects/Test Project', data={
        'name': 'Test Task',
        'priority': 'High',
        'due_date': '2024-12-31',
        'status': 'In Progress',
        'assigned_to': 'Test User'
    }) 

    response = client.post('/delete_task/Test Project', data={'name': 'Test Task'})
    assert response.status_code == 200
    assert b"Task 'Test Task' deleted successfully!" in response.data


def test_delete_project(client):
    """Test deleting a project."""
    client.post('/login')  
    client.post('/dashboard', data={'project_name': 'Test Project'})  

    response = client.post('/delete_project/Test Project')
    assert response.status_code == 200
    assert b"Project 'Test Project' deleted successfully!" in response.data


def test_project_view(client):
    """Test viewing a specific project."""
    client.post('/login')  
    client.post('/dashboard', data={'project_name': 'Test Project'})  

    response = client.get('/projects/Test Project')
    assert response.status_code == 200
    assert b'Test Project' in response.data
    assert b'Tasks' in response.data


def test_about_not_allowed_methods(client):
    """Test if unsupported methods on the about page return 405."""
    response = client.post('/about')  
    assert response.status_code == 405


def test_contact_not_allowed_methods(client):
    """Test if unsupported methods on the contact page return 405."""
    response = client.post('/contact') 
    assert response.status_code == 405
