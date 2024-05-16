function showToast(message) {
    var toastHTML = 
    `<div class="toast" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="2000">
        <div class="toast-header">
            <strong class="me-auto">Notification</strong>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
            ${message}
        </div>
    </div>`;

    var toastContainer = $('.toast-container');
    toastContainer.prepend(toastHTML);
    var toastEl = toastContainer.find('.toast').first();
    var toast = new bootstrap.Toast(toastEl);
    toast.show();
}