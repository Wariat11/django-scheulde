$("#datepicker").datepicker({
  format: "yyyy-mm",
  startView: "months",
  minViewMode: "months"
});
const dateInput = document.getElementById('datepicker');
const submitBtn = document.getElementById('submit-btn');

submitBtn.addEventListener('click', function () {
  const selectedDate = dateInput.value;
  if (selectedDate && selectedDate !== "mm/dd/yyyy") {
    const dateObj = new Date(selectedDate);
    const year = dateObj.getFullYear();
    const month = dateObj.getMonth() + 1;
    const url = `?month=${year}-${month}`;
    window.location.href = url;
  } else {
    event.preventDefault();
  }
});

$(document).ready(function() {
  // Dodajemy event listener dla każdego przycisku .readmore-btn
  $('.readmore-btn').on('click', function() {
    // Dodajemy nową klasę 'readmore-active' dla rodzica przycisku .readmore-btn
    $(this).prevAll('ul').toggleClass('readmore-active');
  });
});

$(".readmore").each(function () {
  var $this = $(this),
    $lis = $this.children(),
    $a = $("<a class='readmore-btn' href='javascript:void(0)'>Zwiń</a>")
  if ($lis.length > 3) {
    $this.after($a);
    $a.click(function () {
      $lis.slice(3).toggle();
      $a.html($a.html() === "Rozwiń" ? "Zwiń" : "Rozwiń")
    }).click();
  }
});

$(document).ready(function () {
  $("body").tooltip({
    selector: '[data-toggle=tooltip]'
  });
});

$(document).ready(function () {
  $(document).on("click", "#modal-btn", function (ev) {
    ev.preventDefault();
    var url = $(this).data('url');
    $.ajax({
      //contentType: 'application/json; charset=utf-8',
      dataType: 'json',
      type: "GET",
      url: url,

      success: function (data) {
        console.log(data);

        $('.modal-title').html('<h2>' + data.service + '</h2>');
        $('#modal-body').html('<div>Imie i nazwisko:</div>' +
          '<h5>' + data.first_name + '</h5>' +
          '<div>Numer telefonu:</div>' +
          '<h5>' + data.number + '</h5>' +
          '<div>Notatka:</div>' +
          '<p>' + data.description + '</p>' +
          '<p>Data: ' + data.date + '</p>' +
          '<p>Godzina: ' + data.time + '</p>');
        $('.modal-form').attr('action', data.pk + '/delete')
        if ($('.btn-delete').length) {
          return;
        }
        $('.modal-form').append('<button type="submit" class="btn-delete btn btn-danger" data-toggle="tooltip" data-bs-placement="right" title="Usuwa bez konieczności potwierdzania">Usuń</button>')

        $('.modal-footer-btn').html(
          '<a href="' + data.pk + '/update"  class="btn btn-primary mr-2">Edytuj</a>' +
          '<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Zamknij</button>');
        $(".modal-form button[data-bs-dismiss]").on("click", () => $("#modal-body").remove())
        $('.modal').modal('show');
      }
    });
  });
});