// DOM Elements
const form = document.getElementById("dashboard-form");
const taskInput = document.getElementById("task-input");
const priorityInput = document.getElementById("priority-input");
const dueDateInput = document.getElementById("due-date-input");
const statusInput = document.getElementById("status-input");
const assignedToInput = document.getElementById("assigned-to-input");
const taskList = document.getElementsByClassName("dashboard-task-list")[0];
const response = document.getElementsByClassName("dashboard-response")[0];
const addTaskButton = document.getElementById("add-task");
const clearTasksButton = document.getElementById("clear-tasks");

// Array to store tasks
let dashboardTasks = [];

// Fetches tasks from localStorage and renders them on the page
const getTasks = function (dashboardTasks) {
    // Clear existing tasks in the UI
    taskList.innerHTML = "";

    // Render each task in the task list
    dashboardTasks.forEach((task, index) => {
        taskList.insertAdjacentHTML(
            "beforeend",
            `
            <div class="dashboard-task">
                <div class="dashboard-task-info">
                    <h6 class="dashboard-task-index">${index + 1}</h6>
                    <p><strong>Name:</strong> ${task.name}</p>
                    <p><strong>Priority:</strong> ${task.priority}</p>
                    <p><strong>Due Date:</strong> ${task.due_date}</p>
                    <p><strong>Status:</strong> ${task.status}</p>
                    <p><strong>Assigned To:</strong> ${task.assigned_to}</p>
                </div>
                <div class="dashboard-task-icons">
                    <i class="far fa-check-circle complete-task"></i>
                    <i class="far fa-edit edit-task"></i>
                    <i class="far fa-times-circle delete-task"></i>
                </div>
            </div>
            `
        );
        // Handle task events (completed, edit, delete)
        handleTask(task.name);
    });
};

// Handles task actions such as completing, editing, and deleting
const handleTask = function (taskName) {
    const tasks = taskList.querySelectorAll(".dashboard-task");

    tasks.forEach((task) => {
        // Match the task name (case-insensitive)
        if (
            task
                .querySelector("p:first-of-type")
                .textContent.trim()
                .toLowerCase()
                .includes(taskName.trim().toLowerCase())
        ) {
            // Completed event: toggle completion status
            task.querySelector(".complete-task").addEventListener("click", function () {
                task.classList.toggle("completed");
            });

            // Edit event: pre-fill task input and remove the task from the list
            task.querySelector(".edit-task").addEventListener("click", function () {
                addTaskButton.innerHTML = "Edit Task"; // Change button text

                // Find the task object and pre-fill the inputs
                const taskToEdit = dashboardTasks.find(
                    (t) => t.name.toLowerCase() === taskName.toLowerCase()
                );

                taskInput.value = taskToEdit.name;
                priorityInput.value = taskToEdit.priority;
                dueDateInput.value = taskToEdit.due_date;
                statusInput.value = taskToEdit.status;
                assignedToInput.value = taskToEdit.assigned_to;

                // Remove task from the list
                dashboardTasks = dashboardTasks.filter((t) => t.name !== taskName);
                setLocalStorage(dashboardTasks); // Save updated tasks
                getTasks(dashboardTasks); // Re-render tasks
            });

            // Delete event: confirm and delete the task
            task.querySelector(".delete-task").addEventListener("click", function () {
                if (confirm("Are you sure you want to delete this task?")) {
                    dashboardTasks = dashboardTasks.filter((t) => t.name !== taskName); // Remove from array
                    setLocalStorage(dashboardTasks); // Save updated tasks
                    getTasks(dashboardTasks); // Re-render tasks
                }
            });
        }
    });
};

// Add task to the list and save to localStorage
form.addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent form submission

    const task = {
        name: taskInput.value.trim(),
        priority: priorityInput.value,
        due_date: dueDateInput.value,
        status: statusInput.value,
        assigned_to: assignedToInput.value.trim(),
    };

    if (!task.name) {
        sendResponse("Please enter a task name", "red"); // Show error response
        return;
    }

    dashboardTasks.push(task); // Add task to array
    addTaskButton.innerHTML = "Add Task"; // Reset button text
    setLocalStorage(dashboardTasks); // Save to localStorage
    getTasks(dashboardTasks); // Re-render tasks
    sendResponse("Task added to dashboard", "green"); // Show success response

    // Clear form inputs
    taskInput.value = "";
    priorityInput.value = "Low";
    dueDateInput.value = "";
    statusInput.value = "Pending";
    assignedToInput.value = "";
});

// Save tasks to localStorage
const setLocalStorage = function (dashboardTasks) {
    localStorage.setItem("dashboardTasks", JSON.stringify(dashboardTasks));
};

// Load tasks from localStorage and display them
const getLocalStorage = function () {
    const dashboardStorage = localStorage.getItem("dashboardTasks");

    if (dashboardStorage === null || dashboardStorage === "undefined") {
        dashboardTasks = []; // If no tasks, initialize as empty array
    } else {
        dashboardTasks = JSON.parse(dashboardStorage); // Parse stored tasks
        getTasks(dashboardTasks); // Display tasks
    }
};

// Initial load of tasks from localStorage
getLocalStorage();

// Display response message (e.g., success or error feedback)
function sendResponse(text, className) {
    response.classList.add(className);
    response.innerHTML = text;

    // Reset response message after 2 seconds
    setTimeout(() => {
        response.classList.remove(className);
        response.innerHTML = "Write value for task name";
    }, 2000);
}

// Clear all tasks when the clear button is clicked
clearTasksButton.addEventListener("click", function () {
    if (confirm("Are you sure you want to clear all tasks?")) {
        dashboardTasks = []; // Clear tasks array
        setLocalStorage(dashboardTasks); // Save empty tasks array
        getTasks(dashboardTasks); // Clear UI
    }
});
