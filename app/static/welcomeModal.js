document.addEventListener('DOMContentLoaded', (event) => {
    var myModal = new bootstrap.Modal(document.getElementById('welcomeModal'), {
      keyboard: false
    });
    myModal.show();
  });  
