$(window).scroll(function() {
    if ($(document).scrollTop() > 600 && $("#myModal").attr("displayed") === "False") {
      $('#myModal').modal('show');
      $("#myModal").attr("displayed", "True");
    }
  });