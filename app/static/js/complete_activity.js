document.addEventListener('DOMContentLoaded', function() {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    document.querySelectorAll('.complete-activity').forEach(function(element) {
        element.addEventListener('click', function() {
            const activityRow = this.closest('.row');
            const activityId = activityRow.getAttribute('data-id');
            console.log(`Attempting to complete activity with id: ${activityId}`);

            fetch(`/complete_activity/${activityId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken // Pass CSRF token in the headers
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log(`Activity with id: ${activityId} completed successfully.`);
                    activityRow.remove();
                } else {
                    console.error(data.error || 'An error occurred while completing the activity.');
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});