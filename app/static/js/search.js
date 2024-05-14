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
  $("#itemlist").append(response);
};

$(function () {
  // On page load, we send an ajax request to the server to get all valid items.
  // We then render the list of items on the page using the renderlistitems function.
  $.ajax({
    type: "GET",
    url: "/search",
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
      type: "GET",
      url: "/search",
      data: {
        search: $("input").val(),
      },
      success: function (response) {
        renderlistitems(response);
      },
    });
  });
});
