#coding:utf-8

from userManager.models import UserProfile,LoginInfo,LogoutInfo,UserdelInfo,UsermodifyInfo,PwdgetInfo,PwdmodifyInfo
from django.shortcuts import render_to_response
from django.template import RequestContext
from userManager.forms import LoginUserForm,AddUserForm,EditUserForm,PwdReapplyForm
from smartcloud.common.CommonPaginator import SelfPaginator
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, EmailMessage
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from log.log import MessageLog
import datetime
import conf
import random
#import sys
#sys.path.append("../..")
#import settings
from django.conf import settings

LOG = MessageLog("/var/log/smartcloud/smartcloud.log")
email_host_user = getattr(settings, "EMAIL_HOST_USER")

def login(request):
	form=None
	if request.method == 'GET' and request.GET.has_key('next'):
		next = request.GET['next']
        else:
                next = '/'
	
	if request.method=="GET":
		form=LoginUserForm()
		return render_to_response('login.html',{"form":form,'next':next},RequestContext(request))
	else:
		form = LoginUserForm(request.POST)
		if form.is_valid():
			data=form.cleaned_data
			login_user=auth.authenticate(username=data['username'],password=data['password'])
			if login_user :
				if(login_user.is_active):
					auth.login(request,login_user)
					info='Login successfully'
					LoginInfo.objects.create(username=data['username'],time=datetime.datetime.now(),info=info)
					if(login_user.is_superuser):
						roleId = None
					else:
						roleId = UserProfile.objects.get(user_id=login_user.id).role_id
						
				#return HttpResponseRedirect(request.POST['next'])
				#return HttpResponseRedirect(reverse())
					request.session['roleId']=roleId
					if(roleId == None):
						return render_to_response('admin/home.html',RequestContext(request))
					elif roleId==1:
						LOG.INFO("user login")
						request.session['base']="user/baseside.html"
						return render_to_response('user/home.html',RequestContext(request))
					elif roleId==2:
						request.session['base']="operator/baseside.html"
						return render_to_response('operator/home.html',RequestContext(request))
					#return render_to_response('home.html',RequestContext(request))
				else:
					info = 'login failed, user is not active.'
					message = '用户未激活'
					LoginInfo.objects.create(username=data['username'],time=datetime.datetime.now(),info=info)
					return render_to_response('login.html',{'form':form,'message':message},RequestContext(request))
					
			else:
				info='Login failed, incorrect username or password.'
				message = '账号或密码错误'
				LoginInfo.objects.create(username=data['username'],time=datetime.datetime.now(),info=info)
				return render_to_response('login.html',{'form':form,'message':message},RequestContext(request))
		else:
			return render_to_response('login.html',{"form":form,'request':request},RequestContext(request))

@login_required
def logoutUser(request):
	    if request.user.is_authenticated():
	   	 LogoutInfo.objects.create(username=request.user,time=datetime.datetime.now())
	    auth.logout(request)
	    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def listUser(request):
	users = UserProfile.objects.all()
        #分页功能
	lst = SelfPaginator(request,users, 2)
        kwvars = {
                  'lPage':lst,
		  'request':request,
		 }
        return render_to_response('admin/userlist.html',kwvars,RequestContext(request))

@login_required
def editUser(request,ID):
	if request.method=='POST':
		form = EditUserForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			print data['is_active']
			user = User.objects.get(id=ID)
			User.objects.filter(id=ID).update(email=data['email'],is_active=data['is_active'])
			UserProfile.objects.filter(user_id=ID).update(name=data['username'],phone=data['phone'],
					role=data['role'],company=data['company'])
			info = 'Modified successfully'
			UsermodifyInfo.objects.create(username=user.username,modify_time=datetime.datetime.now(),result=True,info=info)
			return HttpResponseRedirect(reverse('listuserurl'))
	else:
		user = User.objects.get(id=ID)
		userprofile=UserProfile.objects.get(user_id=ID)
		form = EditUserForm({'username':userprofile.name,'email':user.email,'phone':userprofile.phone,
			'company':userprofile.company.id,'role':userprofile.role.id,'is_active':user.is_active})
	return render_to_response('admin/useredit.html',{"ID":ID,"form":form},RequestContext(request))

@login_required
def deleteUser(request,ID):
	user = User.objects.get(id=ID)
	user.delete()
	UserProfile.objects.filter(user_id=ID).delete()
	info='Removed successfully'
	UserdelInfo.objects.create(username=user.username,time=datetime.datetime.now(),info=info)	
	return HttpResponseRedirect(reverse('listuserurl'))

@login_required
def addUser(request):
         if request.method=='POST':
		 form = AddUserForm(request.POST)
		 if form.is_valid():
			 data=form.cleaned_data
			 email=data['email']
			 name=data['username']
			 password=data['password']
			 phone=data['phone']
			 company=data['company']
			 role=data['role']
			 is_active=data['is_active']
			 user = User(email=email,username=email,is_active=is_active)
			 user.set_password(password)
			 user.save()
			 UserProfile.objects.create(user_id=user.id,name=name,phone=phone,company_id=company,role_id=role)
			 return HttpResponseRedirect(reverse('listuserurl'))
 	 else:
		 form = AddUserForm()
	 kwvars = {
		      'form':form,
		      'request':request,
		      }
     	 return render_to_response('admin/useradd.html',kwvars,RequestContext(request))

@csrf_exempt
def forgetPwd(request):
	if request.method == 'POST':
		form = PwdReapplyForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			username = data['email']
			if User.objects.filter(username=username, is_active=1):
               			 try:
                   			 user = User.objects.get(username=username)
                   			 email = user.email
                   			 number = str(random.randint(100000,999999))
                   			 request.session['number'] = number
                   			 request.session['username_pwd'] = username
                   			 authcode_expire = getattr(conf, 'AUTHCODE_EXPIRT')
                   			 request.session.set_expiry(authcode_expire)
                   			 time_now = datetime.datetime.now()
					 context = '<html><p>Dear '+email+':<br><br>A lost password request has been submitted for your account on '+ str(time_now)[0:19] +'. We have set up a temporary authorization code for your account at '+ email +'.<br>Please login at <a href="http://www.cloud.nite.org.cn/pwd_authcode.html">http://www.cloud.nite.org.cn/pwd_authcode.html</a> as soon as possible and change the password to something you will remember.<br>Your authorization code is <span style="font-size:18px; color:#0088CC; font-size:bold;">'+number+'</span>.The code will expire in 12 hours.<br><br><br><br>--The Stackinsider Team.<br>This is an automatically generated email, please do not reply.</p></html>'
					 msg = EmailMessage('[Stackinsider]The request to lost password.', context,email_host_user, [email])
					 msg.content_subtype = "html"
                   			 msg.send()
                    			 time_now = datetime.datetime.now()
                   			 pwdgetInfo = PwdgetInfo(username=username, request_time=time_now, update_time=time_now)
                    			 pwdgetInfo.save()
                    			 request.session['pwdget_id'] = pwdgetInfo.id
                    			 return render_to_response('user/pwd_authcode.html', RequestContext(request))
                		 except Exception, e:
                    			info = "find password failed, reason: %s" % (e)
                    			time_now = datetime.datetime.now()
					pwdgetInfo = PwdgetInfo(username=username,  request_time=time_now, info=info, update_time=time_now)
                    			pwdgetInfo.save()
                    			message = 'System error, please try again!'
                    			error = True
                    			form = PwdReapplyForm()
                    			message = "Send email failed, please retry again later."
                    			return render_to_response('user/pwd_get.html',{'form':form, "message":message, "error":error},RequestContext(request))
		else:
			message = '您的账户不存在，请重新输入正确的账户.'
                	info = "find password failed, account is not found"
                	time_now = datetime.datetime.now()
                	pwdgetInfo = PwdgetInfo( request_time=time_now, info=info, update_time=time_now)
                	pwdgetInfo.save()
                	error = True
                	return render_to_response('user/pwd_get.html',{'error':error, 'message':message, 'form':form}, RequestContext(request))	
	else:
		form = PwdReapplyForm()
		return render_to_response('user/pwd_get.html', {'form':form},RequestContext(request))

@csrf_exempt
def checkNumber(request):
    if request.is_ajax and request.method == 'POST':
        input_number = request.POST.get('number')
        print input_number	
        if input_number:
            if 'number' in request.session:
                session_number = request.session['number']
        	print session_number	
                if input_number == session_number:
                    return HttpResponse(simplejson.dumps({'status':'success'}))
                else:
                    return HttpResponse(simplejson.dumps({"status":"false"}))
            else:
                return HttpResponse(simplejson.dumps({"status":"expired"}))
        else:
            return HttpResponse(simplejson.dumps({"status":"false"}))

@csrf_exempt
def setPwd(request):
    if request.is_ajax and request.method == 'POST':
        newPasswd = request.POST.get('newPasswd')
        if "username_pwd" in request.session:
            try:
                username = request.session['username_pwd']
                pwdget_id = request.session['pwdget_id']
                user = User.objects.get(username=username)
                user.set_password(newPasswd)
                user.save()
                pwdgetInfo = PwdgetInfo.objects.get(id=pwdget_id)
                pwdgetInfo.result = True
                pwdgetInfo.info = "retrieve password success"
                pwdgetInfo.update_time = datetime.datetime.now()
                pwdgetInfo.save()
               # LOG.INFO("%s retrieve password success" % (username))
		base_url = getattr(conf, "BASE_URL")                
		setpwd_url = base_url + "set_pwd_success/"
                return HttpResponse(simplejson.dumps({'status':setpwd_url}))
            except Exception, e:
                #LOG.INFO("Set pwd failed, reason: %s" % (str(e)))
                return HttpResponse(simplejson.dumps({'status':"false"}))

def setPwdSuccess(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            username = request.user.username
            return render_to_response("user/resetpwd_success.html",{"user":user})
        else:
            return render_to_response('user/resetpwd_success.html')

@login_required
def getUserinfo(request):
   if request.method == 'POST':
	name = request.POST.get('name')
	phone = request.POST.get('phone')
    	up = UserProfile.objects.get(user_id = request.user.id)
	up.name = name
	up.phone = phone
	up.save()
	message = '修改成功！'
	return render_to_response("user/userinfoedit.html",{'userprofile':up,'message':message},RequestContext(request))
   else:
	userprofile = UserProfile.objects.get(user_id=request.user.id) 
    	return render_to_response("user/userinfoedit.html",{'userprofile':userprofile},RequestContext(request))

@csrf_exempt
def changePassword(request):
    	if request.method == 'POST':
          pre_pwd = request.POST.get("pre_pwd")
          new_pwd = request.POST.get("new_pwd")
          if pre_pwd and new_pwd:
            if request.user.is_authenticated():
                user = auth.authenticate(username=request.user.username, password=pre_pwd)
                if user:
                    user.set_password(new_pwd)
                    user.save()
                    time_now = datetime.datetime.now()
                    info = "modify password success"
                    pwdmodifyInfo = PwdmodifyInfo(modify_time=time_now, username=request.user, result=True, info=info)
                    pwdmodifyInfo.save()
                    #LOG.INFO("%s reset password success" % (request.user.username))
                    return HttpResponse(simplejson.dumps({"status":"success"}))
                else:
                    #LOG.ERROR("%s reset password failed, reason: pre password is wrong" % (request.user.username))
                    return HttpResponse(simplejson.dumps({"status":"false"}))
            else:
                return HttpResponse(simplejson.dumps({'status':'logout'}))
	else:
    	    return render_to_response("user/changepwd.html",RequestContext(request))
		
