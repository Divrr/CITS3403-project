document
  .getElementById("offerRequestForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission
    var formData = new FormData(this);
    fetch("/form", {
      // The route that handles your form submission in Flask
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          alert("Your activity has been created!");
          window.location.href = document.body.getAttribute("data-index-url"); // Redirects to the index URL fetched from the data attribute in the body tag
        } else {
          alert("Failed to create activity. Please try again.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("An error occurred. Please try again.");
      });
  });

function changeColor(selectObj) {
  var idx = selectObj.selectedIndex;
  var option = selectObj.options[idx];
  var formContainer = document.querySelector(".form-container");
  var formLabels = document.querySelectorAll(".mb-3 .inputdescription");
  var submitButton = document.querySelector(".submit-btn");

  if (option.value === "Offer") {
    formContainer.style.backgroundColor = "rgb(200 237 251)";
    formContainer.style.borderColor = "rgb(43 114 191)";
    formLabels.forEach(function (label) {
      label.style.color = "#074d97";
    });
    submitButton.style.borderColor = "#2283ea";
  } else if (option.value === "Request") {
    formContainer.style.backgroundColor = "rgb(255 220 177)";
    formContainer.style.borderColor = "rgb(155 108 59)";
    formLabels.forEach(function (label) {
      label.style.color = "rgb(151 74 0)";
    });
    submitButton.style.borderColor = "#f48a18";
  }
}
