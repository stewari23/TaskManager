# Selenium Testing Lab

## 1. Objective
The goal of this lab is to teach students how to use Selenium for UI testing. By completing this lab, students will learn how to write automated scripts to simulate user interactions, verify UI components, and validate web page functionality. Selenium is a powerful tool that helps ensure that the front end of the Task Management System works seamlessly.

## 2. Pre-requisites
- Python 3.x installed on your system.
- Selenium installed in your Python environment.
- A basic understanding of Python programming.
- Basic knowledge of HTML and CSS.
- Google Chrome (or another preferred browser) and the corresponding WebDriver.

## 3. Setup Instructions
### Step 1: Install Selenium
1. Ensure your virtual environment is activated. If not, run:
    ```bash
    source .venv/bin/activate   # For macOS/Linux
    venv\\Scripts\\activate     # For Windows
    ```

2. Install Selenium via pip:
    ```bash
    pip install selenium
    ```

### Step 2: Install Browser Driver

- Run a simple script to ensure Selenium is set up correctly:
    ```python
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    print(driver.title)
    driver.quit()
    ```

- This script should open Chrome, navigate to Google, print the page title, and close the browser.

## 4. Lab Steps
### Step 1: Writing a Simple UI Test Case
- Create a Python file named selenium_test_app.py in your tests/ui/ folder.

- Here is a provided script that includes various Selenium test cases to test core functionalities of the Task Management System:
    
    ```python
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service

    service = Service("C:\\chromedriver\\chromedriver.exe")
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

    # Run tests sequentially
    try:
    test_login()
    test_create_project()
    # Additional tests can be added here
    finally:
    driver.quit()  # Ensure the driver quits at the end
    ```

- This script includes tests for login, project creation, task addition, task deletion, and project deletion. It serves as a comprehensive example of how to automate the core functionality of the Task Management System.

### Step 2: Running the Test
- Run the script using Python:
    ```python
    python tests/ui/selenium_test_app.py
    ```

- Observe the browser automation and verify if the tests pass as expected.

### Step 3: Enhancing the Test
- Update the script to include additional edge cases, such as:
    - Incorrect login credentials.
    - Attempting to add a project without a name.
    - Adding a task with an invalid due date.

## 5. Assessment
- Task 1: Write a Selenium script to test the sign-up functionality of the Task Management System.
- Task 2: Modify the provided test cases to include more validation scenarios (e.g., blank input fields, special characters, incorrect data).
- Task 3: Submit your test scripts and screenshots of the test runs.

## 6. Deliverables
- Scripts: Submit the completed Selenium test scripts.
- Screenshots: Include screenshots showing successful test runs and errors encountered.

## 7. FAQ
- Q: What if the browser doesn’t open?
- A: Ensure that the WebDriver is correctly installed and is compatible with your browser version.

- Q: How do I locate different elements on the webpage?
- A: Use browser developer tools (e.g., right-click > Inspect in Chrome) to find element names, IDs, and XPaths.

## 8. Conclusion
By completing this lab, you should now be comfortable using Selenium to automate UI tests for web applications. You have learned how to write scripts to verify the login functionality, handle errors, and expand your tests to cover additional scenarios.