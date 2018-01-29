$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;


	$('#user_name').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	$('#cpwd').blur(function() {
		check_cpwd();
	});

	$('#email').blur(function() {
		check_email();
	});


	function check_user_name(){
		var len = $('#user_name').val().length;
		if(len<3||len>20)
		{
			$('#user_name').next().html('请输入3-20个字符的用户名')
			$('#user_name').next().show();
			error_name = true;
		}
		else
		{
			 var user = $('#user_name').val();
            $.get("/usercenter/check_username/",{username:user}, function (data) {
                if (data.count != 0) {
                    $('#user_name').next().html("用户名已经存在");
                    $('#user_name').next().show();
                    error_name = true;
                    console.log(error_name)
                } else {
                    $('#user_name').next().hide();
                    error_name = false;
                }
            });
		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致')
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
			error_check_password = true;
		}

	}


	$('#reg_form').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});



    var $h = $(window).height();
    var $margin = $h/2-224;
	$('#register_con').height($h);
	$('.reg_title').css({marginTop:$margin});
	$(".header").css({opacity:1, top:0});








})