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
        const email = document.getElementById('emailInput').value.trim();

        if (username && password && email) {
            // Check if the email has the correct extension
            const emailExtension = getEmailExtension(email);
            if (emailExtension === 'student.uwa.edu.au'_) {
                // Check if the username already exists
                const existingUser = checkExistingUser(username);
                if (existingUser) {
                    alert('Username already exists. Please choose a different username.');
                } else {
                    // Add new entry to authtable.csv
                    addToAuthTable(username, password);
                    localStorage.setItem('loggedIn', 'true');
                    showTaskForm();
                }
            } else {
                alert('Invalid email extension. Please enter a valid email address.');
            }
        } else {
            alert('Please enter username, password, and email');
        }
    });

    function getEmailExtension(email) {
        const emailParts = email.split('.');
        return emailParts[emailParts.length - 1];
    }
    