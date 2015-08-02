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
    var url = '/analyze/twitter/'+username+'/scrapped';
    $("<img/>")
      .on('load', function() { $load.fadeOut(); })
      .on('error', function() { console.log("error loading image"); })
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
