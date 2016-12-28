#!/usr/bin/env python
#-*- coding: utf-8 -*-

from django import forms
from django.contrib import auth
from django.contrib.auth.models import User 
from userManager.models import Company,RoleList
from captcha.fields import CaptchaField

class LoginUserForm(forms.Form):
    username = forms.CharField(label=u'账 号',error_messages={'required':u'账号不能为空'},
        widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=u'密 码',error_messages={'required':u'密码不能为空'},
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    user_cache=None


class AddUserForm(forms.Form):
	email = forms.CharField(label=u'邮 箱',error_messages={'required':u'邮箱不能为空','invalid':'请输入邮箱邮箱'},
       		 widget=forms.TextInput(attrs={'class':'form-control'}))
        username = forms.CharField(label=u'姓 名',
       		 widget=forms.TextInput(attrs={'class':'form-control'}))
    	password = forms.CharField(label=u'密 码',error_messages={'required':u'密码不能为空'},
        	widget=forms.PasswordInput(attrs={'class':'form-control'}))
    	phone = forms.CharField(label=u'手机号',required=False,
        	widget=forms.TextInput(attrs={'class':'form-control'}))
    	company = forms.CharField(label=u'公 司',required=False,
        	widget=forms.Select(choices=((c.id,c.name) for c in Company.objects.all()),attrs={'class':'form-control'}))
    	role = forms.CharField(label=u'角 色',required=False,
        	widget=forms.Select(choices=((r.id,r.name) for r in RoleList.objects.all()),attrs={'class':'form-control'}))
    	is_active = forms.BooleanField(label=u'状 态',required=False,
        	widget=forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}))
	
class EditUserForm(forms.Form):
	email = forms.CharField(label=u'邮 箱',error_messages={'required':u'邮箱不能为空','invalid':'请输入邮箱邮箱'},
       		 widget=forms.TextInput(attrs={'class':'form-control'}))
        username = forms.CharField(label=u'姓 名',
       		 widget=forms.TextInput(attrs={'class':'form-control'}))
#    	password = forms.CharField(label=u'密 码',error_messages={'required':u'密码不能为空'},
 #       	widget=forms.PasswordInput(attrs={'class':'form-control'}))
    	phone = forms.CharField(label=u'手机号',required=False,
        	widget=forms.TextInput(attrs={'class':'form-control'}))
    	company = forms.CharField(label=u'公 司',required=False,
        	widget=forms.Select(choices=((c.id,c.name) for c in Company.objects.all()),attrs={'class':'form-control'}))
    	role = forms.CharField(label=u'角 色',required=False,
        	widget=forms.Select(choices=((r.id,r.name) for r in RoleList.objects.all()),attrs={'class':'form-control'}))
    	is_active = forms.BooleanField(label=u'状 态',required=False,
        	widget=forms.Select(choices=((True, u'启用'),(False, u'禁用')),attrs={'class':'form-control'}))

class AddCompanyForm (forms.Form):
	name = forms.CharField(label=u'公司名称',error_messages={'required':u'公司名称不能为空'},
       		 widget=forms.TextInput(attrs={'class':'form-control'}))

class AddPermissionForm (forms.Form):
	name = forms.CharField(label=u'名称',error_messages={'required':u'权限名称不能为空'},
       		 widget=forms.TextInput(attrs={'class':'form-control'}))
	url = forms.CharField(label=u'URL',error_messages={'required':u'URL不能为空'},
       		 widget=forms.TextInput(attrs={'class':'form-control'}))

class EditRolePermissionForm (forms.ModelForm):
	class Meta:
       		 model = RoleList
       		 widgets = {
           		 'name' : forms.TextInput(attrs={'class':'form-control'}),
           		 'permission' : forms.SelectMultiple(attrs={'class':'form-control','size':'10','multiple':'multiple'}),
       		 }

   	def __init__(self,*args,**kwargs):
       		 super(EditRolePermissionForm,self).__init__(*args,**kwargs)
       		 self.fields['name'].label=u'名 称'
       		 self.fields['name'].error_messages={'required':u'请输入名称'}
       		 self.fields['permission'].label=u'URL'
       		 self.fields['permission'].required=False

class PwdReapplyForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'id':'email'}))
    captcha = CaptchaField()
