document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll(".delete-task-button");

    deleteButtons.forEach((button) => {
        button.addEventListener("click", (e) => {
            e.preventDefault(); // Prevent form submission
            const taskName = button.getAttribute("data-name");

            if (confirm(`Are you sure you want to delete "${taskName}"?`)) {
                const form = button.closest("form");
                fetch(form.action, {
                    method: "POST",
                    body: new FormData(form),
                })
                    .then((response) => response.json())
                    .then((data) => {
                        alert(data.message || "Task deleted successfully.");
                        location.reload(); // Reload the page to update the UI
                    });
            }
        });
    });

    // Handle task addition via the form
    const taskForm = document.getElementById("dashboard-form");
    if (taskForm) {
        taskForm.addEventListener("submit", (e) => {
            e.preventDefault();
            const formData = new FormData(taskForm);

            fetch(taskForm.action, {
                method: "POST",
                body: formData,
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.error) {
                        alert(data.error);
                    } else {
                        alert(data.message || "Task added successfully.");
                        location.reload(); // Reload to show the new task
                    }
                });
        });
    }
});

document.addEventListener("DOMContentLoaded", () => {
    const editButtons = document.querySelectorAll(".edit-task-toggle");
    const editForms = document.querySelectorAll(".edit-task-form");

    // Toggle edit form visibility
    editButtons.forEach((button, index) => {
        button.addEventListener("click", () => {
            const form = editForms[index];
            form.classList.toggle("hidden");
        });
    });

    // Handle task editing
    editForms.forEach((form) => {
        form.addEventListener("submit", (e) => {
            e.preventDefault();

            fetch(form.action, {
                method: "POST",
                body: new FormData(form),
            })
                .then((response) => response.json())
                .then((data) => {
                    alert(data.message || "Task updated successfully.");
                    location.reload(); // Reload to show the updated task
                });
        });
    });
});
