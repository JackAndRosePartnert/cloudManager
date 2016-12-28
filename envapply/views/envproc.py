#coding:utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from smartcloud.common.CommonPaginator import SelfPaginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect 
from django.core.urlresolvers import reverse
from django.db.models import Q
from envapply.models import EnvApplyApprove
from userManager.models import UserProfile
import datetime


def applyEnv(request):
	if request.method == 'GET':
		return render_to_response('user/envapply.html',RequestContext(request))
	else:
		envname = request.POST.get("envname")
		envtype = request.POST.get("envtype")
		if envname and envtype:
			now = datetime.datetime.now()
			EnvApplyApprove.objects.create(apply_user_id =request.user.id,status=0,apply_time=now,approve_time=now,approve_user_id = request.user.id,env_name = envname,apply_env_id=envtype)
			return HttpResponseRedirect(reverse('listapplyurl'))
		return render_to_response('user/envapply.html',RequestContext(request))

@login_required
def listApply(request):
	roleId = UserProfile.objects.get(user_id=request.user.id).role_id
	if 1==roleId:
		applyList =EnvApplyApprove.objects.filter(apply_user_id=request.user.id)
		lst = SelfPaginator(request,applyList, 8)
		kwvars = {
              		'lPage':lst,
            		'request':request, 
       			}        
		return render_to_response('user/applylist.html',kwvars,RequestContext(request))
	else:
		applyList =EnvApplyApprove.objects.filter(status=0)
		lst = SelfPaginator(request,applyList, 8)
		kwvars = {
              	'lPage':lst,
            	'request':request, 
       		}	        
		return render_to_response('operator/notapprovedlist.html',kwvars,RequestContext(request))

def listApproved(request):
		applyList =EnvApplyApprove.objects.exclude(status=0)
		lst = SelfPaginator(request,applyList, 8)
		kwvars = {
              		'lPage':lst,
            		'request':request, 
       			}        
		return render_to_response('operator/appprovedlist.html',kwvars,RequestContext(request))

@login_required
def approve(request,ID,status):
	now = datetime.datetime.now()
	EnvApplyApprove.objects.filter(id=ID).update( status=status, approve_time=now, approve_user=request.user )
	return HttpResponseRedirect(reverse('listapplyurl'))
