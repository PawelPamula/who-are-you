$(document).ready(function(){
  var $twitterForm = $('.home-form');
  var $home = $('.home');
  var $load = $('.home-loading');
  $load.hide();
  $home.addClass('home-middle');

  $twitterForm.on('submit', function(ev) {
    ev.preventDefault();
    var username = $('.twitter-username').val();
  });

  function getHeight() {
    $('.home').height(
      $(window).height() - 1
    );
  };

  $(window).on('resize', getHeight);
  $(window).trigger('resize');

  $('.twitter-username').on('change', function(ev) {
    $home.removeClass('home-middle');
    $home.addClass('home-top');
    $load.fadeIn();
  });
});
