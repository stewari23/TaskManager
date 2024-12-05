document.addEventListener("DOMContentLoaded", () => {
    // Handle project addition
    const projectForm = document.getElementById("project-form");
    if (projectForm) {
        projectForm.addEventListener("submit", (e) => {
            e.preventDefault();
            const formData = new FormData(projectForm);

            fetch(projectForm.action, {
                method: "POST",
                body: formData,
            })
                .then((response) => response.json())
                .then((data) => {
                    alert(data.message || "Project added successfully.");
                    location.reload(); // Reload to show the new project
                });
        });
    }

    // Handle project deletion
    const deleteProjectForms = document.querySelectorAll(".delete-project-form");

    deleteProjectForms.forEach((form) => {
        form.addEventListener("submit", (e) => {
            e.preventDefault(); // Prevent default form submission
            const projectName = form.closest("li").querySelector(".dashboard-task-name").textContent.trim();

            if (confirm(`Are you sure you want to delete the project "${projectName}"?`)) {
                fetch(form.action, {
                    method: "POST",
                })
                    .then((response) => response.json())
                    .then((data) => {
                        alert(data.message || "Project deleted successfully.");
                        location.reload(); // Reload the page to update the project list
                    });
            }
        });
    });
});
