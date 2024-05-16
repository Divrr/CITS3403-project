document.addEventListener('DOMContentLoaded', (event) => {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    document.querySelectorAll('.unaccept-activity').forEach(button => {
        button.addEventListener('click', function () {
            const activityRow = this.closest('.row');
            const activityId = activityRow.getAttribute('data-id');
            console.log(`Attempting to unaccept activity with id: ${activityId}`);

            fetch(`/unaccept/${activityId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken // Pass CSRF token in the headers
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    showToast(data.success)
                    activityRow.remove();
                } else {
                    showToast(data.error || 'Error canceling accept');

                }
            });
        });
    });
});