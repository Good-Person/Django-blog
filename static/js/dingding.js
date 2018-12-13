
$(function () {
    $('.ding-btn').click(function(){
      var $selected = $("select option:selected");
      var $text = $(":text");
      var aname = new Array();
      var ainfo = new Array();
      $selected.each(function(){
        aname.push($(this).val());
      });
      $text.each(function(){
        ainfo.push($(this).val());
      });
      var data = {
        data:{}
      };
      for (var i = 0; i < aname.length; i++) {
        data['data'][aname[i]] = ainfo[i]
      }
      console.log(data);
    })
});




