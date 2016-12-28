#coding:utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from userManager.forms import AddPermissionForm
from userManager.models import PermissionList
from smartcloud.common.CommonPaginator import SelfPaginator
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def listPermission(request):
	permissions = PermissionList.objects.all()
        #分页功能
	lst = SelfPaginator(request,permissions, 2)
        kwvars = {
                  'lPage':lst,
		  'request':request,
		 }
        return render_to_response('admin/permissionlist.html',kwvars,RequestContext(request))

@login_required
def editPermission(request,ID):
	if request.method=='POST':
		form = AddPermissionForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			PermissionList.objects.filter(id=ID).update(name = data['name'],url=data['url'])
			return HttpResponseRedirect(reverse('listpermissionurl'))
	else:
		permission = PermissionList.objects.get(id=ID)
		formvars = {
				'name':permission.name,
				'url':permission.url
				}
		form = AddPermissionForm(formvars)
		return render_to_response('admin/permissionedit.html',{'ID':ID,'form':form},RequestContext(request))
			
@login_required
def deletePermission(request,ID):
	permission = PermissionList.objects.get(id=ID)
	permission.delete()
#	info = 'Removed successfully'
#	PermissiondelInfo.objects.create(name=permission.name,time=datetime.datetime.now(),info = info)
	return HttpResponseRedirect(reverse('listpermissionurl'))

@login_required
def addPermission(request):
	if request.method=='POST':
		form = AddPermissionForm(request.POST)
	        if form.is_valid():
		        data=form.cleaned_data
			name=data['name']
                        url = data['url']
			PermissionList.objects.create(name=name,url=url)
		        return HttpResponseRedirect(reverse('listpermissionurl'))
        else:
                form = AddPermissionForm()
	kwvars={
		'form':form,
		'request':request
			}
     	return render_to_response('admin/permissionadd.html',kwvars,RequestContext(request))
