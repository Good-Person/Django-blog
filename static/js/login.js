$(function () {

    var $h = $(window).height();
    var $margin = $h/2-175;
	$('#login_con').height($h);
	$('#login_form').css({marginTop:$margin});
	$(".header").css({opacity:1, top:0});

});