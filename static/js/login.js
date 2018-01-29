$(function () {

    var $h = $(window).height();
    var $margin = $h/2-175;
    var $jparticle =$("#jparticle-container");
	$('#login_con').height($h);
	$jparticle.height($h-70);
	$('#login_form').css({marginTop:$margin});
	$(".header").css({opacity:1, top:0});


	// 来个一次函数控制点的数量。
	var slope = (1400-375)/(100-20);
	var $ww = $(window).width();
	var spotNum = parseInt($ww/slope);


	$jparticle.jParticle({
	  particlesNumber: spotNum,
	  linkDist: 50,
	  createLinkDist: 150,
	  disableLinks: false,
	  disableMouse: false,
	  background: "#222222",
	  color: "white",
	  width: null,
	  height: null,
	  linksWidth: 1,
	  particle: {
		color: "white",
		minSize: 2,
		maxSize: 4,
		speed: 60
	  }
	});
});