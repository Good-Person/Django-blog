$(function () {
    var scrollTop = $(window).scrollTop();

    $(document).scroll(function () {
       var nowTop = $(document).scrollTop();
       if (nowTop>400){
           $("#toTop").css({opacity:0.7});
       }
       else {
           $("#toTop").css({opacity:0});
       }

       if (nowTop>scrollTop){
           $('#header').css({'top':-70, 'opacity':0});
           scrollTop = nowTop;
       }
       else{
           $('#header').css({'top':0, 'opacity':1});
           scrollTop = nowTop;
       }

    });


    $("#toTop").click(function () {
        $('html,body').animate({
            "scrollTop": 0
        });
    });

    $(".header").css({opacity:1, top:0});
    $(".content").css({marginTop:'100px'});



});