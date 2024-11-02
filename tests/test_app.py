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

