$(function () {

    var $h = $(window).height();
    var $headerContent = $("#header-content");
    var $down = $("#header-content span");

    //导航条添加点击事件
    $(".navbar-nav li").click(
            function () {
                $(this).siblings().removeClass("active");
                $(this).addClass("active");
            }
    );

    //设置header图片、动画的行高
    $("#header-image").height($h);
    $("#effect").height($h);
    //设置图片中的文本位置
    $headerContent.height($h);
    var hch = $("#header-content div").height();
    $headerContent.children().css({'marginTop': -hch});
    //图片中文本动画
    $headerContent.addClass('moving');
    //导航的动画设置
    $(document).scroll(function () {
        var $top = $(document).scrollTop();
        var num = $top/$h*1.3;
        if($top>20){
            $('#header').css({'top':0, 'opacity':1});
            $headerContent.children().css({'marginTop': 0});
            $headerContent.removeClass('moving');
            $down.hide()
        }
        else {
            $headerContent.addClass('moving');
            $headerContent.children().css({'marginTop': -hch});
            $('#header').css({'top':-70, 'opacity':0});
            $down.show()
        }
        $("#effect").css({'opacity':num});

        if($top>400){
            $("#toTop").css({'opacity':0.7});
        }
        else {
            $("#toTop").css({'opacity':0});
        }

    });

    //实时控制巨幕图片大小
    $(window).resize(function () {
        $h = $(window).height();
        $("#header-image").height($h);
        $("#effect").height($h);
        $headerContent.height($h);
        hch = $("#header-content div").height();
        $headerContent.children().css({'marginTop': -hch});
    });



    $("#toTop").click(function () {
        $('html,body').animate({
            "scrollTop": 0
        });
    });












});