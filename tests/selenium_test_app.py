import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


service = Service("C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

def test_login():
    """Test user login functionality."""
    driver.get("http://127.0.0.1:5000/login") 
    assert "Login" in driver.title

    # Fill and submit the login form
    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("testpassword")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(2)  # Allow time for the page to load
    assert "Dashboard" in driver.page_source


def test_create_project():
    """Test project creation functionality."""
    driver.get("http://127.0.0.1:5000/dashboard")
    assert "Task Management Dashboard" in driver.title

    # Fill and submit the 'Create Project' form
    driver.find_element(By.ID, "project-name").send_keys("New Test Project")
    driver.find_element(By.ID, "add-project").click()

    # Handle the alert
    WebDriverWait(driver, 10).until(EC.alert_is_present())  # Wait until the alert is present
    alert = driver.switch_to.alert  # Switch to the alert
    alert_text = alert.text
    assert "Project 'New Test Project' added successfully!" in alert_text
    alert.accept() 

    # Verify the project is displayed on the dashboard
    time.sleep(2)  # Allow time for the page to refresh
    assert "New Test Project" in driver.page_source


def test_add_task():
    """Test task addition to a project."""
    driver.get("http://127.0.0.1:5000/projects/New%20Test%20Project")
    assert "Manage Tasks" in driver.title

    # Fill and submit the 'Add Task' form
    driver.find_element(By.ID, "task-input").send_keys("Test Task")
    driver.find_element(By.ID, "priority-input").send_keys(Keys.DOWN)
    driver.find_element(By.ID, "due-date-input").send_keys("2024-12-31")
    driver.find_element(By.ID, "status-input").send_keys(Keys.DOWN)
    driver.find_element(By.ID, "assigned-to-input").send_keys("Tester")
    driver.find_element(By.ID, "add-task").click()

    # Handle the alert
    WebDriverWait(driver, 10).until(EC.alert_is_present())  # Wait until the alert is present
    alert = driver.switch_to.alert  # Switch to the alert
    alert_text = alert.text
    assert "Task 'Test Task' added successfully!" in alert_text 
    alert.accept()  

    # Verify the task is displayed
    time.sleep(2)
    assert "Test Task" in driver.page_source


def test_delete_task():
    """Test deleting a task from a project."""
    # Navigate to the project page
    driver.get("http://127.0.0.1:5000/projects/New%20Test%20Project")
    assert "Manage Tasks" in driver.title

    # Add a task for deletion
    driver.find_element(By.ID, "task-input").send_keys("Task to Delete")
    driver.find_element(By.ID, "priority-input").send_keys("Medium")
    driver.find_element(By.ID, "due-date-input").send_keys("2024-12-31")
    driver.find_element(By.ID, "status-input").send_keys("Pending")
    driver.find_element(By.ID, "assigned-to-input").send_keys("Tester")
    driver.find_element(By.ID, "add-task").click()

    # Handle the success alert for task creation
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    # Locate and delete the task
    delete_button = driver.find_element(By.CSS_SELECTOR, "form button.delete-task-button[data-name='Task to Delete']")
    delete_button.click()

    # Handle the confirmation alert
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert "Are you sure you want to delete" in alert_text
    alert.accept()

    # Handle the success alert for task deletion
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert "Task 'Task to Delete' deleted successfully!" in alert_text
    alert.accept()

    # Verify the task is no longer listed
    time.sleep(2)
    assert "Task to Delete" not in driver.page_source


def test_update_task():
    """Test updating a task in a project."""
    # Navigate to the project page
    driver.get("http://127.0.0.1:5000/projects/New%20Test%20Project")
    assert "Manage Tasks" in driver.title

    # Add a task for updating
    driver.find_element(By.ID, "task-input").send_keys("Task to Update")
    driver.find_element(By.ID, "priority-input").send_keys("Low")
    driver.find_element(By.ID, "due-date-input").send_keys("2024-12-31")
    driver.find_element(By.ID, "status-input").send_keys("Pending")
    driver.find_element(By.ID, "assigned-to-input").send_keys("Tester")
    driver.find_element(By.ID, "add-task").click()

    # Handle the success alert for task creation
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    # Locate and click the 'Edit' button for the task
    edit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Edit')]")
    edit_button.click()

    # Update the task details
    form = driver.find_element(By.CSS_SELECTOR, "form.edit-task-form")
    form.find_element(By.NAME, "name").clear()
    form.find_element(By.NAME, "name").send_keys("Updated Task Name")
    form.find_element(By.NAME, "priority").send_keys("High")
    form.find_element(By.NAME, "due_date").clear()
    form.find_element(By.NAME, "due_date").send_keys("2024-11-30")
    form.find_element(By.NAME, "status").send_keys("In Progress")
    form.find_element(By.NAME, "assigned_to").clear()
    form.find_element(By.NAME, "assigned_to").send_keys("Updated Tester")
    form.find_element(By.CSS_SELECTOR, ".save-task-button").click()

    # Handle the success alert for task update
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert "Task 'Task to Update' updated successfully!" in alert_text
    alert.accept()

    # Verify the task details are updated on the page
    time.sleep(2)
    assert "Updated Task Name" in driver.page_source
    assert "High" in driver.page_source
    assert "2024-11-30" in driver.page_source
    assert "In Progress" in driver.page_source
    assert "Updated Tester" in driver.page_source


def test_delete_project():
    """Test project deletion functionality."""
    driver.get("http://127.0.0.1:5000/dashboard")

    # Locate and delete the project
    delete_button = driver.find_element(By.CSS_SELECTOR, "form.delete-project-form button")
    delete_button.click()

    # Handle the alert
    WebDriverWait(driver, 10).until(EC.alert_is_present())  # Wait until the alert is present
    alert = driver.switch_to.alert  # Switch to the alert
    alert_text = alert.text
    assert 'Are you sure you want to delete the project "New Test Project"?' in alert_text
    alert.accept()

    WebDriverWait(driver, 10).until(EC.alert_is_present())  # Wait until the alert is present
    alert = driver.switch_to.alert  # Switch to the alert
    alert_text = alert.text
    assert "Project 'New Test Project' deleted successfully!" in alert_text 
    alert.accept()


    # Verify the project is deleted
    time.sleep(2)
    assert "New Test Project" not in driver.page_source


# Run tests sequentially
try:
    test_login()
    test_create_project()
    test_add_task()
    test_delete_project()
finally:
    driver.quit()  # Ensure the driver quits at the end
