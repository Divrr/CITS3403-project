/*
  Response is a list of items that the server returns. Each item is a dictionary with the following fields:
    {
      'id': int,
      'author': "username",
      'acceptor': "username",
      'type': "offer",
      'category': "category",
      'description': "description",
      'status': "open",
      'updated_at': "2021-12-12 12:12:12"
    }
  We currently only require 'category' and 'description' for rendering the list of items on the page, but we may need other fields in the future)
  */

// This script is used to construct the DOM with the list of items that the server returns.
// We loop through the items in response and append them to the itemlist div.
renderlistitems = function (response) {
  $("#itemlist").empty();

  for (let item of response) {
    $("#itemlist").append(`
    <div class="col-lg-3 col-md-4 col-sm-6 g-3">
      <div class="p-4 h-100 text-center d-flex flex-column justify-content-around 
          {% if request.endpoint == 'offers' %} 
          tinypaddingoffers
          {% elif request.endpoint == 'requests' %} 
          tinypaddingrequests
          {% endif %}">

        <div class="h4 fw-semibold text-uppercase">
            ${item.category}
        </div>

        <div class="p fs-6 fst-italic text-start sans-serif text-center">
            ${item.description}
        </div>

        <button type="button" 
            {% if request.endpoint == 'offers' %} 
            id="offeracceptbtn"
            {% elif request.endpoint == 'requests' %} 
            id="requestacceptbtn"
            {% endif %}
            class="btn btn-light btn-sm">
          accept
        </button>
      </div>
    </div>
`);
  }
};

$(function () {
  // On page load, we send an ajax request to the server to get all valid items.
  // We then render the list of items on the page using the renderlistitems function.
  console.log("search.js loaded");
  $.ajax({
    type: "POST",
    url: "",
    data: {
      search: "",
    },
    success: function (response) {
      renderlistitems(response);
    },
  });

  // When the user types in the search bar, we send an ajax request to the server with the search query.
  // We then render the list of items on the page using the renderlistitems function.
  $("input").on("input", function () {
    $.ajax({
      type: "POST",
      url: "",
      data: {
        search: $("input").val(),
      },
      success: function (response) {
        renderlistitems(response);
      },
    });
    return false;
  });
});
