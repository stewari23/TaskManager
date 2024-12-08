
# Postman API Testing Lab

## Objective
This lab aims to teach students how to use **Postman** for API testing. By the end of the lab, students will know how to create, send, and validate HTTP requests for essential endpoints like user sign-up, login, project creation, and task management in the Task Management System.

---

## Pre-requisites
- **Postman** installed on your computer.
- Basic understanding of **HTTP methods** (GET, POST, DELETE).
- Knowledge of JSON and HTTP status codes.
- A running instance of the **Task Management System**.

---

## Setup Instructions
1. **Install Postman**  
   Download and install Postman from [here](https://www.postman.com/downloads/).
   
2. **Run the Task Management System**  
   Start the Task Management application locally. The base URL will be `http://127.0.0.1:5000`.
   ``` bash
   python .\src\app.py
   ```

3. **Create a New Postman Collection**  
   - Open Postman and click `+ New Collection`.
   - Name the collection: **Task Management System API Tests**.
   - Add the following HTTP requests into the collection.

---

## Lab Steps

### Step 1: User Signup

- **Method**: `POST`  
- **Endpoint**: `http://127.0.0.1:5000/signup`  

- **Body**:
  ```
  {
    "username": "newuser",
    "password": "newpassword"
  }
  ```

- **Scripts**:
  ``` Javascript
  pm.test("Status code is 200", function () {
      pm.response.to.have.status(200);
  });

  pm.test("Response contains success message", function () {
      var jsonData = pm.response.json();
      pm.expect(jsonData.message).to.eql("Signup successful. Please log in.");
  });
  ```

- **Expected Response**:
  - **Status Code**: `200`
  - **Body**: Contains `Signup successful. Please log in.`

---

### Step 2: User Login

- **Method**: `POST`  
- **Endpoint**: `http://127.0.0.1:5000/login`  

- **Body**:
  ```
  {
    "username": "testuser",
    "password": "testpass"
  }
  ```

- **Scripts**:
  ``` Javascript
  pm.test("Status code is 302 (redirect)", function () {
      pm.response.to.have.status(302);
  });

  pm.test("Response contains Dashboard header", function () {
      pm.expect(pm.response.text()).to.include("<h1>Create and Manage Projects</h1>");
  });

  // Save the session cookie for authentication
  let sessionCookie = pm.cookies.get('session');
  if (sessionCookie) {
      pm.environment.set("session_cookie", sessionCookie);
  } else {
      console.log("Session cookie not found!");
  }
  ```

- **Expected Response**:
  - **Status Code**: `302`
  - **Redirect Location**: `/dashboard`

- **Note**: Save the session cookie from this request.  
  - In the response, click `Cookies` and save the session cookie for subsequent requests.

---

### Step 3: Create a Project

- **Method**: `POST`  
- **Endpoint**: `http://127.0.0.1:5000/dashboard`  
- **Headers**:  
  - `Content-Type`: `application/x-www-form-urlencoded` 
  
  Use the saved session cookie from Step 2. 
  - `Key`: Cookie
  - `Value`: session={{session_cookie}}   

- **Body**:
  - `Key`: project_name
  - `Value`: Test Project  
  
- **Scripts**:
  ``` Javascript
  pm.test("Status code is 200", function () {
      pm.response.to.have.status(200);
  });

  pm.test("Response contains success message in HTML", function () {
      const responseText = pm.response.text();
      pm.expect(responseText).to.include("Project 'Test Project' added successfully!");
  });
  ```

- **Expected Response**:
  - **Status Code**: `200`
  - **Body**: Contains `Project 'Test Project' added successfully!`.

---

### Step 4: Add a Task

- **Method**: `POST`  
- **Endpoint**: `http://127.0.0.1:5000/projects/Test%20Project`  
- **Headers**:  
  - `Content-Type`: `application/x-www-form-urlencoded`  

  Use the saved session cookie from Step 2. 
  - `Key`: Cookie
  - `Value`: session={{session_cookie}}   

- **Body**:
  - `name`: Test Task
  - `priority`: High
  - `due_date`: 2024-12-31
  - `status`: Pending
  - `assigned_to`: Tester
  
- **Scripts**:
  ``` Javascript
  pm.test("Status code is 200", function () {
      pm.response.to.have.status(200);
  });

  pm.test("Response contains success message", function () {
      const responseText = pm.response.text();
      pm.expect(responseText).to.include("Task 'Task Name' added successfully!");
  });
  ```  

- **Expected Response**:
  - **Status Code**: `200`
  - **Body**: Contains `Task 'Test Task' added successfully!`.

---

### Step 5: Delete the Project

- **Method**: `POST`  
- **Endpoint**: `http://127.0.0.1:5000//delete_project/Test%20Project`  
- **Headers**:  
  - `Content-Type`: `application/x-www-form-urlencoded`  
  
  Use the saved session cookie from Step 2. 
  - `Key`: Cookie
  - `Value`: session={{session_cookie}}  
  
- **Scripts**:
  ``` Javascript
  pm.test("Status code is 200", function () {
      pm.response.to.have.status(200);
  });

  pm.test("Response contains success message", function () {
      pm.response.to.have.body.include("Project 'Test Project' deleted successfully!");
  });
  ```  
  
- **Expected Response**:
  - **Status Code**: `200`
  - **Body**: Contains `Project 'Test Project' deleted successfully!`.

---

## Assessment Tasks
1. **Create a New User**  
   Sign up using a unique username and verify the response.

2. **Attempt Login with Incorrect Credentials**  
   Test the `/login` endpoint with invalid credentials such as missing field and observe the error response. 

3. **Create and Delete a Project**  
   Verify the creation and deletion of a project.

4. **Add Multiple Tasks to a Project**  
   Test adding multiple tasks to the same project and verify each addition.

5. **Submit Evidence**  
   - Save the collection in Postman and export it as a JSON file.
   - Include screenshots of the successful requests and responses.

---

## FAQ
**Q: How can I capture session cookies in Postman?**  
A: After logging in, click the `Cookies` tab in the response. Save the `session` cookie and include it in subsequent requests.

**Q: How do I handle spaces in the project name for the endpoint?**  
A: Replace spaces with `%20`. For example, `Test Project` becomes `Test%20Project`.

**Q: How can I ensure my tests are repeatable?**  
A: Use variables in Postman to store common values like `base_url`, `username`, and `password`.

---

## Deliverables
1. **Postman Collection**: Export your Postman collection as a JSON file and submit it.
2. **Screenshots**: Include screenshots for each successful test case.
3. **Report**: Summarize your results, including any challenges encountered.

By completing this lab, students will gain hands-on experience testing APIs with Postman. They will learn to handle cookies, validate responses, and test CRUD operations effectively.
