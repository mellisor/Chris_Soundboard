function getCookie(name) {
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) == name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        return cookieValue;
      }
    }
  }
}

$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
  }
});

var toDelete;

function showDelete(id) {
  toDelete = id;
  $("#deleteModal").modal("show");
}

function doDelete() {
  var data = serializeById("deleteForm");
  data["id"] = toDelete;
  $.ajax({
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(data),
    success: function() {
      // if parent node consists of category title and this item, delete the category
      if (
        $(`#${toDelete}`)
          .parent()
          .children().length == 2
      ) {
        $(`#${toDelete}`)
          .parent()
          .remove();
      } else {
        $(`#${toDelete}`).remove();
      }
      $("#deleteModal").modal("hide");
    }
  });
}
