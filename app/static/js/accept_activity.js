document.addEventListener('DOMContentLoaded', function () {
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    document.querySelector('#itemlist').addEventListener('click', function (e) {
        if (e.target.classList.contains('acceptbtn')) {
            const activityBox = e.target.parentElement.parentElement;
            const activityId = activityBox.getAttribute('data-id');
            console.log(`Attempting to complete activity with id: ${activityId}`);
            fetch(`/accept/${activityId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken // Pass CSRF token in the headers
                }
            })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        showToast(data.success);
                        activityBox.remove();
                    }
                    else {
                        showToast(data.error);
                    }
                })
                .catch(error => console.error('Error:', error));
        }
    });
});