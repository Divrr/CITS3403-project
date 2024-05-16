document.addEventListener('DOMContentLoaded', (event) => {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    if (document.getElementById('welcomeModal')) {
        var myModal = new bootstrap.Modal(document.getElementById('welcomeModal'), {
            keyboard: false
        });
        myModal.show();

        fetch('/clear_welcome_flag', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken // Pass CSRF token in the headers
            },
            body: JSON.stringify({ show_welcome: false })
        })
            .then(response => {
                if (response.ok) {
                    console.log('Session flag cleared successfully.');
                } else {
                    console.error('Failed to clear session flag.');
                }
            })
            .catch(error => {
                console.error('Error clearing session flag:', error);
            });
    }
});