$(document).ready(function()
{
// Popover 
$('#registerHere input').hover(function()
{
$(this).popover('show');
},function(){
        $(this).popover('hide'); 
});

//testing
/*$("#create_account").click(function(event){
  $("#loading").show();
});*/

// Validation
$("#registerHere").validate({
				rules:{
					firstname:{
							required:true,
						//	minlength: 2,
							maxlength: 16,
						//	remote: "/check/registeruser/"
						},
                    lastname:{
                            required:true,
                        //    minlength: 2,
                            maxlength: 16, 
                        //  remote: "/check/registeruser/"
                        },
					mail:{
							required:true,
							email: true,
							remote:"/check/registerMail"
						},
					social_account:{
							required:true,
							email: true,
							remote:"/check/registerMail"
						},
					pwd:{
						required:true,
						minlength: 6,
						maxlength: 16
					},
					repwd:{
						required:true,
						equalTo: "#pwd"
					},
                    nation:{
                        required:true,
                    }, 
                    industry:{
                        required:true,
                    }, 
                    occupation:{
                        required:true,
                    },
                  /*  age:{
                        required:true,
                    }, */
					captcha_1:{
						required: true,
					},
				},
				messages:{
					firstname:{
                        required:"请输入您的名字",
						//remote: "This username already exists. Please try again."
					},
                    lastname:{
                        required:"请输入您的姓",
                        //remote: "This username already exists. Please try again."
                    },
					mail:{
						required:"请输入您的邮箱地址",
						email:"请输入有效的邮箱地址",
						remote:"该邮箱已注册，请重试"
					},
					social_account:{
						required:"请输入您的邮箱地址",
						email:"请输入有效的邮箱地址",
						remote:"该邮箱已注册，请重试"
					},
					pwd:{
						required:"请输入您的密码",
						minlength:"密码至少要有6个字符"
					},
					repwd:{
						required:"确认您的密码",
						equalTo:"两次输入密码不同，请重新输入"
					},
                    nation:{
                        required:"选择您的国家",
                    },
                    industry:{
                        required:"选择您的行业",
                    },
                    occupation:{
                        required:"选择您的职业",
                    },
                    /*age:{
                        required:"Select your age",
                    },*/
					captcha_1:{
						required:"请输入验证码",
					},
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
				}
			});


$("#step_form01").validate({
                rules:{
                    email:{
                        required:true,
						email: true,	
                       // remote: "/check/pwdGet/"
                    }, 
                    captcha_1:{
                        required: true,
                    },  
                },  
                messages:{
                    email:{
                        required:"请输入您的邮箱地址",
						email: "请输入有效的邮箱地址",
                        //remote:"Please input the right Email"
                    }, 
                    captcha_1:{
                        required:"请输入验证码",
                    }, 
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
                }   
            });

$("#step_form02").validate({
                rules:{
                    number:{
                        required:true,
                        remote: "/check/number/"
                    },  
                },  
                messages:{
                    number:{
                        required:"请输入授权码",
                        remote:"无效的授权码，请重新输入"
                    },  
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
                }   
            });


$("#step_form03").validate({
                rules:{
                    newPasswd:{
                        required:true,
                        minlength: 6,
                        maxlength: 16
                    },  
                    rePasswd:{
                        required:true,
                        equalTo: "#newPasswd"
                    },  
                },  
                messages:{
                    newPasswd:{
                        required:"请输入密码",
                        minlength:"您的密码至少要有6个字符"
                    },  
                    rePasswd:{
                        required:"请确认您的密码",
                        equalTo:"两次输入密码不同，请重新输入"
                    },  
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
                }   
            });

$("#modify_pwd").validate({
                rules:{
		    new_pwd:{
			remote:"/check/new_pwd",
                        required:true,
                        minlength: 6,
                        maxlength: 16
                    }, 	 
                    re_pwd:{
                        required:true,
                        equalTo: "#new_pwd"
                    },  
                },  
                messages:{
		    new_pwd:{
			remote:"新密码不能和原密码相同",
                        required:"请输入您的新密码",
                        minlength:"密码至少要有6个字符"
                    },
                    re_pwd:{
                        required:"确认密码",
                        equalTo:"两次输入密码不同，请重新输入"
                    },  
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
                }   
            });


$("#update_info").validate({
                rules:{
                    firstname:{
                        required:true,
                        minlength: 1,
                        maxlength: 30,
						//remote: "/check/user_info/"
                    },
                    lastname:{
                        required:true,
                        minlength: 1,
                        maxlength: 30, 
                        //remote: "/check/user_info/"
                    },  
                },
                messages:{
                  /*  firstname:{
                        required:"Please input your nickname.",
                        minlength:"Username must have at least 2 characters.",
						maxlength:"Username must have at most 16 characters.",
						remote:"This username already exists. Please try again."					
                    },*/
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
                }
            });

$("#contactinfo").validate({
            rules:{
                    city:{
                        required:true,
                        minlength: 1,
                        maxlength: 30, 
                    },  
                    country:{
                        required:true,
                        minlength: 1,
                        maxlength: 30, 
                    }, 
                    code:{
                        digits:true,
                    },
                    homenum:{
                        digits:true,
                    },
                    worknum:{
                        digits:true,
                    },
                    mobile:{
                        digits:true,
                    },  
                    fax:{
                        digits:true,
                    }  
                },  
                messages:{
                  /*  firstname:{
                        required:"Please input your nickname.",
                        minlength:"Username must have at least 2 characters.",
                        maxlength:"Username must have at most 16 characters.",
                        remote:"This username already exists. Please try again."                    
                    },*/
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
                } 
            });

$("#professioninfo").validate({
            rules:{
                    employer:{
                        required:true,
                        minlength: 1,
                        maxlength: 30, 
                    },  
                    department:{
                        required:true,
                        minlength: 1,
                        maxlength: 30, 
                    },  
                    title:{
                        required:true,
                    } 
                },  
                messages:{
                  /*  firstname:{
                        required:"Please input your nickname.",
                        minlength:"Username must have at least 2 characters.",
                        maxlength:"Username must have at most 16 characters.",
                        remote:"This username already exists. Please try again."                    
                    },*/
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
                }   
            }); 


$("#project_form").validate({
                rules:{
                    project_name:{
                        required:true,
                        minlength: 3,
                        maxlength: 50, 
                     //   remote: "/check/project_name/"
                    },  
                },  
                messages:{
                    project_name:{
                        required:"创建用户名",
                        minlength:"用户名至少要有3个字",
                        maxlength:"用户名最多只能有16个字",
                     //   remote:"This username already exists. Please try again."    
                    },  
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
                }
            });

$("#signinHere").validate({
                rules:{
                    user:{
                        required:true,
						email:true,
                        minlength: 3
                     //   maxlength: 16
                    },  
                    passwd:{
                        required:true,
                        minlength: 6,
						maxlength: 16
                    },
                    captcha_1:{
                        required:true,
                    }  
                },  
                messages:{
                    user:{
                        required:"请输入您的账号",
						email:"请输入有效的邮箱地址",
                        minlength:"用户名至少要有3个字"
					//	maxlength:"The username must be at most 16 characters"
                    },  
                    passwd:{
                        required:"请输入密码",
						minlength:"密码至少要有6个字",
						maxlength:"密码最多要有16个字"		
                    },
                    captcha_1:{
                        required:"请输入验证码"
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
                }   
            }); 
$("#sendmsg").validate({
                rules:{
                    firstname:{
                        required:true,
                        minlength: 1,
                        maxlength: 16,
                    },
                    lastname:{
                        required:true,
                        minlength: 1,
                        maxlength: 16, 
                    }, 
                    email:{
                        required:true,
                        email: true,
                    },  
                    subject:{
                        required:true,
                        minlength: 3,
                        maxlength: 50, 
                    },  
                    message:{
                        required:true,
                        minlength: 3,
                        maxlength: 2000, 
                    },  
                },  
                messages:{
                    firstname:{
                        required:"请输入您的名字",
                        minlength:"名字至少有1个字",
                        maxlength:"名字最多有16个字",
                    }, 
                    lastname:{
                        required:"请输入您的姓",
                        minlength:"姓至少有1个字",
                        maxlength:"姓最多有16个字",
                    },
                    email:{
                        required:"请输入您的邮箱",
                    },  
                    subject:{
                        required:"请输入您的主题",
                        minlength:"主题至少要有3个字",
                        maxlength:"主题最多有50个字",
                    },  
                    message:{
                        required:"请输入内容",
                        minlength:"内容至少有3个字",
                        maxlength:"内容最多有2000个字",
                    },  
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
                }   
            });

$("#survey").validate({
               /* rules:{
                    explain18:{
                        required:true,
                        minlength: 5,
                    },  
                    explain17:{
                        required:true,
                        minlength: 5,
                    },  
                    explain9:{
                        required:true,
                        minlength: 5,
                    },  
                    explain8:{
                        required:true,
                        minlength: 5,
                    }, 
                    explain7:{
                        required:true,
                        minlength: 5,
                    }, 
                },  
                messages:{
                    explain18:{
                        required:"Please explain.",
                    },  
                    explain17:{
                        required:"Please explain.",
                    },  
                    explain9:{
                        required:"Please explain",
                    },  
                    explain8:{
                        required:"Please explain.",
                    },  
                    explain7:{
                        required:"Please explain.",
                    }, 
                },*/  
                errorClass: "error",
                errorElement: "label",
                highlight:function(element, errorClass, validClass) {
                    $(element).parents('.control-group').removeClass('success');
                    $(element).parents('.control-group').addClass('error');
                },  
                unhighlight: function(element, errorClass, validClass) {
                    $(element).parents('.control-group').removeClass('error');
                    $(element).parents('.control-group').addClass('success');
                }
            });

//footer
});
