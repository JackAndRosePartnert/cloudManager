#coding:utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from userManager.forms import EditRolePermissionForm
from userManager.models import RoleList,PermissionList
from smartcloud.common.CommonPaginator import SelfPaginator
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def listRole(request):
	permissions = RoleList.objects.all()
        #分页功能
	lst = SelfPaginator(request,permissions, 2)
        kwvars = {
                  'lPage':lst,
		  'request':request,
		 }
        return render_to_response('admin/rolelist.html',kwvars,RequestContext(request))

@login_required
def editRolePermission(request,ID):
	role = RoleList.objects.get(id=ID)
	if request.method=='POST':
		form =EditRolePermissionForm(request.POST,instance=role)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('listroleurl'))
	else:
		form = EditRolePermissionForm(instance=role)
		return render_to_response('admin/roleedit.html',{'form':form,'ID':ID},RequestContext(request))
			

