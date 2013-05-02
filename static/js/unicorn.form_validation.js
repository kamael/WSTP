/**
 * Unicorn Admin Template
 * Diablo9983 -> diablo9983@gmail.com
**/
$(document).ready(function(){
	
	$('input[type=checkbox],input[type=radio],input[type=file]').uniform();
	
	$('select').chosen();
	
	// Form Validation
	// 
    $("#all_validate").validate({
    			rules:{
			required:{
				required:true
			},
			email:{
				required:true,
				email: true,
				remote:{
					type:"GET",
					url:"/check/email/",
					data:{
						email:function()
						{
							return $("#email").val();
						}
					}
				}
			},
			username:{
				required:true,
				number:true,
				rangelength:[9,9],
				remote:{
					type:"GET",
					url:"/check/username/",
					data:{
						username:function()
						{
							return $("#username").val();
						}
					}
				}

			},
			password:{
				required: true,
				minlength:6,
				maxlength:20
			},
			pwd2:{
				required:true,
				minlength:6,
				maxlength:20,
				equalTo:"#password"
			}

		},
		errorClass: "help-inline",
		errorElement: "span",
		highlight:function(element, errorClass, validClass) {
			$(element).parents('.control-group').removeClass('success');
			$(element).parents('.control-group').addClass('error');
		},
		unhighlight: function(element, errorClass, validClass) {
			$(element).parents('.control-group').removeClass('error');
			$(element).parents('.control-group').addClass('success');
		},
		messages: {
			username:{
				required:"请输入一卡通",
				number:"一卡通为 9 位数字",
				rangelength:"一卡通为 9 位数字",
				remote:"该一卡通已经被注册,如有疑问请联系xxxxx!"
			},
			password:{
				required:"请输入密码",
				minlength:"密码至少 6 位",
				maxlength:"密码至多 20 位"
			},
			pwd2:{
				required:"请再次输入密码",
				minlength:"密码至少 6 位",
				maxlength:"密码至多 20 位",
				equalTo:"请输入相同密码"
			},
			email:{
				required:"请输入E-mail",
				email: "请输入正确格式",
				remote:"该 E-mail 已经被注册"
			}
		}
	});

});
