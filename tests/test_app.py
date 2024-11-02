import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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


def test_signup(client):
    """Test if the signup page loads correctly."""
    response = client.get('/signup')
    assert response.status_code == 200
    assert b'Sign Up' in response.data