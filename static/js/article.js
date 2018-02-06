$(function () {
    var scrollTop = $(window).scrollTop();
    var aid = $(".ajax-post span").html();
    var csrf = $(".ajax-post input:first-child").val();
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


    // 获取回复

    $.ajax({
        type:'get',
        url:"/comment/get_reply/",
        data:{'aid':aid},
        dataType:'json',
        success:function(data){
            $.each(data.reply, function (i, item) {
                pid = '#'+item.pid;
                content = item.html;
                $(pid).append(content);

            });
        }
    });




    // 提交按钮
    $("#comments").delegate("button", "click", function () {
        var content = $(this).parent().children('textarea').val();
        var pid = $(this).parent().parent().attr('id');

        if (content.length==0){
            alert('内容不能为空、、、');
            return
        }

        if (pid == 'comments'){

            $.ajax({
                type:'post',
                url:"/comment/add/",
                data:{'csrfmiddlewaretoken':csrf,'aid':aid,'content':content},
                dataType:'json',
                success:function(){
                    window.location.reload();
                }
            });
        }
        else {
            $.ajax({
                type:'post',
                url:"/comment/addreply/",
                data:{'csrfmiddlewaretoken':csrf,'aid':aid,'content':content,'parent':pid},
                dataType:'json',
                success:function(){
                    window.location.reload();
                }
            });
        }


    });



    // 回复按钮
    var $replySwitch = false;
    $('.comment-content').delegate("a","click", function () {
        if ($replySwitch){
            $(this).html('回复').parent().children('textarea').remove();
            $(this).parent().children('button').remove();
            $replySwitch = false;
        }
        else {
            content = $('.button-comment').html();
            $(this).html('取消').parent().append(content);
            $replySwitch = true;
        }
    });



    // 来个一次函数控制评论框高
    var slope = (1400-375)/(200-80);
	var $ww = $(window).width();
    theight = ($ww-33)/slope;
    $('.comments textarea').height(theight);
});