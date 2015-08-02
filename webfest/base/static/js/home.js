$(document).ready(function(){
  // Home height equal to viewport
  //Home page get twitter name
  var $twitterForm = $('.home-form');

  $twitterForm.on('submit', function(ev) {
    ev.preventDefault();
    var username = $('.twitter-username').val();
    location.href = "/analyze/twitter/"+ username;
  });

  function getHeight() {
    $('.home').height(
      $(window).height() - 1
    );
  };

  $(window).on('resize', getHeight);
  $(window).trigger('resize');
});
