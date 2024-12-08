
# Test Coverage Report

This test coverage report evaluates the test cases based on the test plan, which requires:
- **Unit Testing**: Validate individual components.
- **Integration Testing**: Ensure interactions between different modules.
- **System Testing**: Verify the entire system’s functionality.
- **Acceptance Testing**: Confirm that the application meets user requirements.

---

## 1. Unit Testing

Unit testing focuses on validating individual components or endpoints of the application.

### Covered Tests:
- **Pytest Tests:**
  - **`test_index`**: Validates that the homepage loads correctly.
  - **`test_about`**: Ensures the "About" page loads correctly.
  - **`test_contact`**: Ensures the "Contact Us" page loads correctly.
  - **`test_login`**: Confirms that the login page loads correctly.
  - **`test_login_post_success`**: Verifies that POST to `/login` redirects properly.
  - **`test_signup_post_success`**: Ensures that signup POST requests return the correct success message.

### Coverage:
- Individual Flask routes and their responses were validated in isolation.
- Core application components (e.g., `/login`, `/signup`, `/dashboard`) were tested.

---

## 2. Integration Testing

Integration testing ensures different components (e.g., frontend, backend, database) work together.

### Covered Tests:
- **Pytest Integration Tests:**
  - **`test_dashboard`**: Verifies that the dashboard integrates with the login session.
  - **`test_add_project`**: Tests integration between project creation and the dashboard display.
  - **`test_add_task`**: Ensures proper integration between tasks and their associated projects.
- **Selenium Tests:**
  - **`test_login`**: Verifies that user login integrates the frontend form submission with backend authentication.
  - **`test_create_project`**: Confirms project creation integrates with the dashboard display.
  - **`test_add_task`**: Ensures tasks are added to the correct project and displayed in the UI.

### Coverage:
- Validated integration points between Flask routes, the session system, and the UI.
- Confirmed proper data flow between frontend forms, backend logic, and UI updates.

---

## 3. System Testing

System testing verifies the functionality of the entire system.

### Covered Tests:
- **Selenium Tests:**
  - **`test_create_project`**: End-to-end test for creating and displaying a project.
  - **`test_add_task`**: End-to-end test for adding tasks to a project and verifying the display.
  - **`test_delete_project`**: End-to-end test for deleting a project and ensuring it no longer appears on the dashboard.
- **Postman Tests:**
  - API tests to validate that backend routes handle various conditions (e.g., successful project creation, validation errors).

### Coverage:
- Simulated real-world usage by executing workflows across the application (e.g., creating a project, adding tasks, deleting a project).
- Verified complete functionality of the project and task management system.

---

## 4. Acceptance Testing

Acceptance testing ensures the application meets user requirements and expectations.

### Covered Tests:
- **Selenium Tests:**
  - **`test_create_project`**: Confirms that project creation aligns with user expectations (e.g., alert messages, dashboard updates).
  - **`test_add_task`**: Ensures the task addition workflow meets user needs.
  - **`test_delete_task`**: Confirms that tasks can be deleted and the UI updates accordingly.
- **Postman Tests:**
  - Validates that API endpoints produce correct outputs for expected inputs, aligning backend functionality with user requirements.

### Coverage:
- Verified user-facing features (e.g., task and project management) behave as expected.
- Confirmed the application provides user-friendly error handling and success messages.

---

## Test Coverage Summary

| Test Category       | Tools Used         | Coverage                                                   |
|---------------------|--------------------|-----------------------------------------------------------|
| **Unit Testing**    | Pytest             | Validated individual Flask routes and components.          |
| **Integration Testing** | Pytest, Selenium | Verified integration between backend logic and the UI.     |
| **System Testing**  | Selenium, Postman  | Tested complete workflows across the application.          |
| **Acceptance Testing** | Selenium, Postman | Ensured compliance with user requirements and expectations.|

---

## Recommendations
- Continue maintaining the separation of tests for better modularity and easier debugging.
- Expand Postman tests for edge cases in API endpoints.

