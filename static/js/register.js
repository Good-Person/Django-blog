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
	$('#reg_form').css({marginTop:$margin+65});
	$('.reg_title').css({marginTop:$margin});
	$(".header").css({opacity:1, top:0});


	// 蜂巢动画
	var w = c.width = window.innerWidth,
		h = c.height = window.innerHeight,
		ctx = c.getContext( '2d' ),

		opts = {

		  len: 20,
		  count: 50,
		  baseTime: 10,
		  addedTime: 10,
		  dieChance: .05,
		  spawnChance: 1,
		  sparkChance: .1,
		  sparkDist: 10,
		  sparkSize: 2,

		  color: 'hsl(hue,100%,light%)',
		  baseLight: 50,
		  addedLight: 10, // [50-10,50+10]
		  shadowToTimePropMult: 6,
		  baseLightInputMultiplier: .01,
		  addedLightInputMultiplier: .02,

		  cx: w / 2,
		  cy: h / 2,
		  repaintAlpha: .04,
		  hueChange: .1
		},

		tick = 0,
		lines = [],
		dieX = w / 2 / opts.len,
		dieY = h / 2 / opts.len,

		baseRad = Math.PI * 2 / 6;

	ctx.fillStyle = 'black';
	ctx.fillRect( 0, 0, w, h );

	function loop() {

	  window.requestAnimationFrame( loop );

	  ++tick;

	  ctx.globalCompositeOperation = 'source-over';
	  ctx.shadowBlur = 0;
	  ctx.fillStyle = 'rgba(0,0,0,alp)'.replace( 'alp', opts.repaintAlpha );
	  ctx.fillRect( 0, 0, w, h );
	  ctx.globalCompositeOperation = 'lighter';

	  if( lines.length < opts.count && Math.random() < opts.spawnChance )
		lines.push( new Line );

	  lines.map( function( line ){ line.step(); } );
	}
	function Line(){

	  this.reset();
	}
	Line.prototype.reset = function(){

	  this.x = 0;
	  this.y = 0;
	  this.addedX = 0;
	  this.addedY = 0;

	  this.rad = 0;

	  this.lightInputMultiplier = opts.baseLightInputMultiplier + opts.addedLightInputMultiplier * Math.random();

	  this.color = opts.color.replace( 'hue', tick * opts.hueChange );
	  this.cumulativeTime = 0;

	  this.beginPhase();
	}
	Line.prototype.beginPhase = function(){

	  this.x += this.addedX;
	  this.y += this.addedY;

	  this.time = 0;
	  this.targetTime = ( opts.baseTime + opts.addedTime * Math.random() ) |0;

	  this.rad += baseRad * ( Math.random() < .5 ? 1 : -1 );
	  this.addedX = Math.cos( this.rad );
	  this.addedY = Math.sin( this.rad );

	  if( Math.random() < opts.dieChance || this.x > dieX || this.x < -dieX || this.y > dieY || this.y < -dieY )
		this.reset();
	}
	Line.prototype.step = function(){

	  ++this.time;
	  ++this.cumulativeTime;

	  if( this.time >= this.targetTime )
		this.beginPhase();

	  var prop = this.time / this.targetTime,
		  wave = Math.sin( prop * Math.PI / 2  ),
		  x = this.addedX * wave,
		  y = this.addedY * wave;

	  ctx.shadowBlur = prop * opts.shadowToTimePropMult;
	  ctx.fillStyle = ctx.shadowColor = this.color.replace( 'light', opts.baseLight + opts.addedLight * Math.sin( this.cumulativeTime * this.lightInputMultiplier ) );
	  ctx.fillRect( opts.cx + ( this.x + x ) * opts.len, opts.cy + ( this.y + y ) * opts.len, 2, 2 );

	  if( Math.random() < opts.sparkChance )
		ctx.fillRect( opts.cx + ( this.x + x ) * opts.len + Math.random() * opts.sparkDist * ( Math.random() < .5 ? 1 : -1 ) - opts.sparkSize / 2, opts.cy + ( this.y + y ) * opts.len + Math.random() * opts.sparkDist * ( Math.random() < .5 ? 1 : -1 ) - opts.sparkSize / 2, opts.sparkSize, opts.sparkSize )
	}
	loop();

	window.addEventListener( 'resize', function(){

	  w = c.width = window.innerWidth;
	  h = c.height = window.innerHeight;
	  ctx.fillStyle = 'black';
	  ctx.fillRect( 0, 0, w, h );

	  opts.cx = w / 2;
	  opts.cy = h / 2;

	  dieX = w / 2 / opts.len;
	  dieY = h / 2 / opts.len;



	});


});