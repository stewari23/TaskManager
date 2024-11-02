# Test Plan for Task Manager Application

## 1. Introduction
**Project Overview:** The Task Manager Application is designed to facilitate task and project management for users, allowing functionalities such as user authentication, task and project creation, task assignment, and status tracking. The objective is to ensure that the application meets functional, usability, and reliability standards while adhering to the specified requirements.

**Objective:** The test plan aims to validate the application's functionality, usability, reliability, and compatibility through a combination of manual and automated tests.

## 2. Test Strategy
**Testing Approach:** This test plan will utilize a combination of manual and automated testing. Functional testing will be performed for core features, while automated tests will leverage Pytest, Selenium, Playwright, and Robot Framework to verify user interactions, UI components, and backend processing.

**Test Levels:**
- **Unit Testing:** Validate individual components.
- **Integration Testing:** Ensure interactions between different modules.
- **System Testing:** Verify the entire system’s functionality.
- **Acceptance Testing:** Confirm that the application meets user requirements.

**Risk Analysis:** Potential risks include database failures, authentication issues, and browser compatibility bugs.

## 3. Test Environment
The application will be tested on Windows, macOS, and Linux systems, with various browsers including Chrome, Firefox, and Safari. Testing tools include Pytest, Selenium, Postman, and Robot Framework. Collaboration and tracking will be done through GitHub and MS Teams.

## 4. Test Scope
**In-scope:**
- User Authentication (sign-up, login, password reset)
- Task Management (create, update, delete, and view tasks)
- Project Management features
- Task Assignment and status updates
- Notification functionalities

**Out-of-scope:** Performance testing and load testing are excluded at this stage.

## 5. Test Scenarios
### Scenario 1: User Authentication
- **Pre-condition:** The application is running.
- **Test Steps:** Attempt to sign up, log in, and reset the password.
- **Expected Outcome:** Users can securely sign up, log in, and reset their passwords.

### Scenario 2: Task Creation and Persistence
- **Pre-condition:** User is logged in, and the task list is initially empty.
- **Test Steps:** Create a new task and check that it is displayed and saved.
- **Expected Outcome:** The new task appears in the task list and remains after refresh.

### Scenario 3: Task Update and Deletion
- **Pre-condition:** Task exists in the task list.
- **Test Steps:** Update task details and delete a task.
- **Expected Outcome:** Task updates reflect in the list, and deleted tasks are removed permanently.

## 6. Testing Schedule
**Timeline:**
- **Week 8-11:** Unit testing for core functionalities.
- **Week 11-13:** Integration and system testing.
- **Week 13-15:** Acceptance testing and defect logging.

**Milestones:**
- Completion of unit tests
- System test results review
- Final acceptance test feedback

## 7. Test Deliverables
- Test Plan Document
- Manual and automated test cases
- Bug reports and logs
- Test Summary Report

## 8. Roles and Responsibilities
- **Project Manager:** Oversees and coordinates the testing process.
- **Developers:** Assist in fixing logged defects and ensuring code readiness.
- **Testers:** Execute test cases and report issues.

## 9. Test Data Management
Test data will include sample task and project entries, valid/invalid user credentials, and varied task status conditions. Test data will be managed through mock data stored in JSON or SQLite format.

## 10. Defect Management
Defects will be logged and managed using GitHub. Each defect will be assigned a priority level (critical, high, medium, low) and tracked until resolved.

## 11. Communication and Collaboration
Weekly updates will be shared during team meetings via MS Teams. Test reports and progress will be logged on GitHub.

## 12. Review and Adaptation
The test plan will be reviewed at the end of each testing phase to ensure it aligns with any changes in project scope or requirements.

## 13. Approval
This Test Plan requires approval from the team members: Lacy Fields, Jack Stahl, Shivam Tewari, and Alex Rosa.

