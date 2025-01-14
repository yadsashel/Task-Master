// control the visibility of the navbar menu on mobile
document.addEventListener("DOMContentLoaded", function() {
    const hamburger = document.querySelector(".hamburger");
    const navbarList = document.querySelector(".navbar__list");

    hamburger.addEventListener("click", function() {
        navbarList.classList.toggle("active");
    });
});

//adding and retrieving tasks from the db 
document.addEventListener("DOMContentLoaded", function() {
    const taskForm = document.getElementById("taskForm");
    const taskList = document.getElementById("taskList");

    // Retrieve tasks from localStorage on load
    loadTasks();

    // Handle form submission
    taskForm.addEventListener("submit", function(event) {
        event.preventDefault();
        
        const title = document.getElementById("title").value;
        const description = document.getElementById("description").value;
        const dueDate = document.getElementById("dueDate").value;
        
        const newTask = {
            id: Date.now().toString(),
            title: title,
            description: description,
            due_date: dueDate,
            completed: false
        };

        saveTask(newTask);
        taskForm.reset();
        displayTask(newTask);
    });

    // Save task to localStorage
    function saveTask(task) {
        const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
        tasks.push(task);
        localStorage.setItem("tasks", JSON.stringify(tasks));
    }

    // Load tasks from localStorage
    function loadTasks() {
        const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
        tasks.forEach(displayTask);
    }

    // Display task on the page
    function displayTask(task) {
        const taskElement = document.createElement("div");
        taskElement.classList.add("task");
        taskElement.id = `task-${task.id}`;
        taskElement.innerHTML = `
            <h3 class="task__item-title">${task.title}</h3>
            <p class="task__item-description">${task.description}</p>
            <p class="task__item-due">Due: ${task.due_date}</p>
            <div class="task__buttons">
                <button class="task__edit-button" onclick="editTask('${task.id}')">Edit</button>
                <button class="task__delete-button" onclick="deleteTask('${task.id}')">Delete</button>
                <button class="task__complete-button" onclick="toggleComplete('${task.id}')">${task.completed ? "Unmark" : "Complete"}</button>
            </div>
        `;

        taskList.appendChild(taskElement);
    }

    // Edit task
    window.editTask = function(taskId) {
        const tasks = JSON.parse(localStorage.getItem("tasks"));
        const task = tasks.find(task => task.id === taskId);

        if (task) {
            document.getElementById("title").value = task.title;
            document.getElementById("description").value = task.description;
            document.getElementById("dueDate").value = task.due_date;

            deleteTask(taskId); // Remove the old task before saving the updated one
        }
    };

    // Delete task
    window.deleteTask = function(taskId) {
        let tasks = JSON.parse(localStorage.getItem("tasks"));
        tasks = tasks.filter(task => task.id !== taskId);
        localStorage.setItem("tasks", JSON.stringify(tasks));

        const taskElement = document.getElementById(`task-${taskId}`);
        if (taskElement) {
            taskElement.remove();
        }
    };

    // Toggle task completion
    window.toggleComplete = function(taskId) {
        const tasks = JSON.parse(localStorage.getItem("tasks"));
        const task = tasks.find(task => task.id === taskId);

        if (task) {
            task.completed = !task.completed;
            localStorage.setItem("tasks", JSON.stringify(tasks));

            // Update the button text
            const taskElement = document.getElementById(`task-${taskId}`);
            const completeButton = taskElement.querySelector(".task__complete-button");
            completeButton.textContent = task.completed ? "Unmark" : "Complete";
        }
    };
});