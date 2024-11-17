const form = document.getElementById("dashboard-form")
const taskInput = document.getElementById("task-input")
const taskList = document.getElementsByClassName(".dashboard-task-list")
const response = document.getElementsByClassName(".dashboard-response")
const addTaskButton = document.getElementById("add-task")
const clearTasksButton = document.getElementById("clear-tasks")

let dashboardList = [];

//TODO: Get List

const getTasks = function (dashboardTasks) {
    taskList.innerHTML = "";
    dashboardTasks.forEach((task, index) => { 
        taskList.insertAdjacentHTML("beforeend",
            `
            <div class="dashboard-task">
                    <div class="dashboard-task-info">
                        <h6 class="dashboard-task-index">${index}</h6>
                        <p class="dashboard-task-name">${task}</p>
                    </div>
                    
                    <div class="dashboard-task-icons">
                        <i class="far fa-check-circle complete-task"></i>
                        <i class="far fa-edit edit-task"></i>
                        <i class="far fa-times-circle delete-task"></i>
                    </div>
                </div>
            `
        );
        handleTask(task);
    }); 
};


//TODO: Handle task

const handleTask = function (taskName) {
    const tasks = taskList.querySelectorAll(".dashboard-task")
    tasks.forEach((task) => {

        if(task.querySelector(".dashboard-task-name".textContent.trim().
        toLowerCase()===taskName.trim().toLowerCase())){
            //TODO: Completed event
            //TODO: Edit event
            //TODO: Delete event
        }
    });
}
//TODO: Add item to the list
//TODO: Save and Load to local Storage
//TODO: Send feedback
//TODO: Clear all items.