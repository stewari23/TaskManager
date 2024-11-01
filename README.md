> [!NOTE]
> This is a living document and will change as our Group progresses. 

# Task Management System

## Introduction
The Task Management System is a web application designed to help individuals and teams manage tasks and projects efficiently. It includes user authentication, task and project CRUD operations, task assignments, status tracking, and notification features.

## Team Members
- Project Manager: Lacy Fields
- Front-End Developer: Shivam Tewari
- Back-end Developer: Alex Rosa
- Software Engineer: Jack Stahl

## Installation Instructions
1. Clone the Repository:
```bash
git clone https://github.com/yourusername/fa24project-fa24project_t9.git
```

2. Move to the project directory:
```bash
cd directory name
```

3. Set up the Virtual Environment:
```bash
python3 -m venv venv
```

4. Activate the VENV:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

5. Install Dependencies:
```bash
pip install -r requirements.txt
```

6. Run the Application:
```bash
python src/app.py
```

## Usage Instructions
- After installation, navigate to the app's home page to sign up or log in.
- Create, manage, and assign tasks and projects from the dashboard.
- Access the task assignment, status tracking, and notification features in the navigation bar.

## Technology Stack
- Frontend: HTML, CSS, & JavaScript
- Backend: Python, Flask
- Database: SQLite
- Testing Tools: Pytest, Selenium, Playwright, Postman, & Robot Framework
- Collaboration: MS Teams
- Version Control: GitHub, GitHub Desktop
- CI/CD: GitHub Actions (planned for automated testing and deployment)

## Features and Functionality
- User Authentication: Secure user login, sign-up, and password reset.
- Task Management: Create, update, delete, and view tasks with priority levels and due dates.
- Project Management: Create and manage multiple projects with individual tasks.
- Task Assignment: Assign tasks to users and track their status.
- Status Tracking: View and update task status (e.g., pending, in progress, completed).
- Notifications: Receive in-app notifications for task updates.

## API Endpoints !!! WIP !!!
TBD

## Contribution Guidelines
- Branch Naming: Use clear names like feature/task-crud, bugfix/login-issue.
- Pull Requests: PRs must be approved by at least one team member and include passing tests.
- Code Style: Follow PEP8 for Python code and include comments where necessary.
- Testing: Include relevant unit or integration tests with new features.

## Testing Procedures - !!! WIP !!!
- Unit Tests: Located in the tests/unit/ folder, run with:
```bash
pytest tests/unit
```
- API Testing: Using Postman and Requests library for API endpoint validation.
- UI Testing: Selenium and Playwright scripts in tests/ui/.
- Acceptance Testing: Run acceptance tests in Robot Framework for end-to-end validation.

## License !!! WIP !!!
Specify the license under which the project is released, if applicable.

## Contact Information
- https://github.com/Lacy-Fields

## Acknowledgments
Special thanks to our instructor, Cindy Halliday for guidance and providing resources and templates. And to the members of this team that made an idea reality. Without your grit, this project would have never made it this far.

## Version History/Changelog
- v0.1: Initial project setup with Flask engine
- v0.2: Added project management files and structure
- v0.3: Built templates for app pages and test plans

## Frequently Asked Questions (FAQs) !!! WIP !!!
TBD