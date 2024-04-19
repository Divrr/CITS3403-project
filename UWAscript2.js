document.addEventListener('DOMContentLoaded', function() {
    const authForm = document.getElementById('authForm');
    const taskForm = document.getElementById('taskForm');
    const taskInput = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');

    // Check if the user is logged in
    const isLoggedIn = localStorage.getItem('loggedIn') === 'false';
    if (isLoggedIn) {
        showTaskForm();
    } else {
        authForm.style.display = 'block';
    }

    // Sign up event
    document.getElementById('signupButton').addEventListener('click', function() {
        const username = document.getElementById('usernameInput').value.trim();
        const password = document.getElementById('passwordInput').value.trim();

        if (username && password) {
            localStorage.setItem('username', username);
            localStorage.setItem('password', password);
            localStorage.setItem('loggedIn', 'true');
            showTaskForm();
        } else {
            alert('Please enter both username and password');
        }
    });

    // Task form submission
    taskForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const taskText = taskInput.value.trim();
        if (taskText !== '') {
            addTask(taskText);
            taskInput.value = '';
        }
    });

    function showTaskForm() {
        authForm.style.display = 'none';
        taskForm.style.display = 'block';
    }

    function addTask(taskText) {
        const li = document.createElement('li');
        li.textContent = taskText;

        const assignButton = document.createElement('button');
        assignButton.textContent = 'Assign';
        assignButton.classList.add('assign-button');
        assignButton.addEventListener('click', function() {
            alert('Assigning task: ' + taskText);
            // Here you can implement the assignment logic
        });

        li.appendChild(assignButton);
        taskList.appendChild(li);
    }
});
