document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('.unaccept-activity').forEach(button => {
        button.addEventListener('click', function () {
            const activityId = this.dataset.id;
            fetch(`/unaccept/${activityId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content') // Ensure you include the CSRF token for security
                }
            }).then(response => {
                if (response.ok) {
                    location.reload();
                } else {
                    response.json().then(data => {
                        alert(data.error || 'Error canceling accept');
                    });
                }
            });
        });
    });
});