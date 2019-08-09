var transformDuration = 200;
var opened;

function showCategories() {
  opened = null;
  hideSounds();
  setTimeout(function() {
    $(".catDiv").removeClass("d-none");
    $(".catDiv").hide(0);
    $(".catDiv").show(transformDuration);
  }, transformDuration);
}

function hideSounds() {
  $(`.soundDiv[category!=${opened}]`).hide(transformDuration);
}

function showSounds() {
  $(`.catDiv`).addClass("d-none");
  $(`.soundDiv[category=${opened}`).show(transformDuration);
}

$(function() {
  $(".cat-card,.cat-btn").click(function() {
    var target = $(this).attr("data-target");
    if (target == opened) {
      return;
    } else if (opened == null) {
      opened = $(this).attr("data-target");

      showSounds();
    } else {
      opened = $(this).attr("data-target");
      hideSounds();
      setTimeout(function() {
        showSounds();
      }, transformDuration);
    }
  });
});

function play(path) {
  var audio = new Audio(path);
  audio.play();
}
