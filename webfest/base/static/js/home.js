$(document).ready(function(){
  var $twitterForm = $('.home-form');
  var $home = $('.home');
  var $load = $('.home-loading');
  $load.hide();
  $home.addClass('home-middle');

  $twitterForm.on('submit', function(ev) {
    ev.preventDefault();
    var username = $('.twitter-username').val();
    $home.removeClass('home-middle');
    $home.addClass('home-top');
    $load.fadeIn();
    $('.home-result').empty();
    var url = '/analyze/twitter/'+username+'/scrapped';
    $("<img/>")
      .on('load', function() {
        $load.fadeOut();
        $(window).trigger('resize');
      })
      .on('error', function() {
        $load.fadeOut();
      })
      .attr("src", url).appendTo('.home-result');
  });

  function getHeight() {
    $('.home').height(
      $(window).height() - 1
    );
  };
  $(window).on('resize', getHeight);
  $(window).trigger('resize');
});
