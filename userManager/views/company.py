#coding:utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from userManager.forms import AddCompanyForm
from userManager.models import Company,CompanydelInfo
from smartcloud.common.CommonPaginator import SelfPaginator
from django.contrib import auth
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def listCompany(request):
	companies = Company.objects.all()
        #分页功能
	lst = SelfPaginator(request,companies, 2)
        kwvars = {
                  'lPage':lst,
		  'request':request,
		 }
        return render_to_response('admin/companylist.html',kwvars,RequestContext(request))

@login_required
def editCompany(request,ID):
	if request.method=='POST':
		form = AddCompanyForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			Company.objects.filter(id=ID).update(name = data['name'])
			return HttpResponseRedirect(reverse('listcompanyurl'))
	else:
		company = Company.objects.get(id=ID)
		formvars = {
				'name':company.name
				}
		form = AddCompanyForm(formvars)
		return render_to_response('admin/companyedit.html',{'ID':ID,'form':form},RequestContext(request))
			

@login_required
def deleteCompany(request,ID):
	company = Company.objects.get(id=ID)
	company.delete()
	info = 'Removed successfully'
	CompanydelInfo.objects.create(name=company.name,time=datetime.datetime.now(),info = info)
	return HttpResponseRedirect(reverse('listcompanyurl'))

@login_required
def addCompany(request):
	if request.method=='POST':
		form = AddCompanyForm(request.POST)
	        if form.is_valid():
		        data=form.cleaned_data
			name=data['name']
                        Company.objects.create(name=name,bind_operator=request.user.username)
		        return HttpResponseRedirect(reverse('listcompanyurl'))
        else:
                form = AddCompanyForm()
	kwvars={
		'form':form,
		'request':request
			}
     	return render_to_response('admin/companyadd.html',kwvars,RequestContext(request))
