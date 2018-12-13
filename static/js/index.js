$(function () {

    var limit = 5;
    var start = 5;
    $('.more-article a').click(function () {
        $.ajax({
            type:'get',
            url:"/blog/index/?page_start={0}&page_limit={1}".format(start,limit),
            dataType:'json',
            success:function(data){
                start = start+limit;
                if (data.msg.length === 0) {
                    $('.more-article').hide();
                    alert('已经加载到底了...')
                }
                $.each(data.msg, function (i, item) {
                    content = '<div class="article col-md-8 col-sm-12 col-xs-12"><div class="atitle"><a href="{aurl}">{atitle}</a></div><div class="ainfo clearfix"><ul><li class="fl"><span class="fa fa-user"></span>&nbsp;{user}&nbsp;&nbsp;</li><li class="fl"><span class="fa fa-calendar"></span>&nbsp;{create_date}&nbsp;&nbsp;</li></ul></div><div class="acontent">{summary}</div><div class="afooter"><ul><li class="fl"><span class="fa fa-list-ul"></span>&nbsp;{category}&nbsp;&nbsp;</li><li class="fl"><span class="fa fa-eye"></span>&nbsp;{views}&nbsp;&nbsp;</li><li class="fl"><span class="fa fa-comments"></span>&nbsp;{comment_number}&nbsp;&nbsp;</li></ul></div></div><div class="picture col-md-4 hidden-sm hidden-xs"><div><a href="{aurl}"><img src="{img_link}" alt="配图" class="img-responsive center-block"></a></div></div><div class="col-md-12 col-sm-12 col-xs-12"><hr></div>'.format(item);
                    $('.article-box').append(content);
                    // console.log(content)

                });
            }
        });
    })





});

