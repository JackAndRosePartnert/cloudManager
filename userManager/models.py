#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

#用户删除操作
class UserdelInfo(models.Model):
    username = models.CharField(max_length=50)
    time = models.DateTimeField()
    info = models.CharField(max_length=300)

#公司信息
class Company(models.Model):
    name = models.CharField(max_length=50)
    bind_operator = models.CharField(max_length=50) 
    def __unicode__(self):
        return self.name

#公司删除操作
class CompanydelInfo(models.Model):
    name = models.CharField(max_length=50)
    time = models.DateTimeField()
    info = models.CharField(max_length=300)

#权限信息
class PermissionList(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s(%s)' %(self.name,self.url)

#角色信息                                              
class RoleList(models.Model):
    name = models.CharField(max_length=20)
    permission = models.ManyToManyField(PermissionList,null=True,blank=True)

    def __unicode__(self):
        return self.name

#用户登入记录 
class LoginInfo(models.Model):
    username = models.CharField(max_length=50)
    time = models.DateTimeField()
    info = models.CharField(max_length=300)

#用户登出记录 
class LogoutInfo(models.Model):
    username = models.CharField(max_length=50)
    time = models.DateTimeField()

#用户忘记密码
class PwdgetInfo(models.Model):
    username = models.CharField(max_length=50)
    request_time = models.DateTimeField()
    update_time = models.DateTimeField()
    result = models.BooleanField(blank=True, default=False)
    info = models.CharField(blank=True, max_length=300)

#用户修改密码
class PwdmodifyInfo(models.Model):
    username = models.CharField(max_length=50)
    modify_time = models.DateTimeField()
    result = models.BooleanField(default=True)
    info = models.CharField(max_length=300)

#用户修改个人信息
class UsermodifyInfo(models.Model):
    username = models.CharField(max_length=50)
    modify_time = models.DateTimeField()
    result = models.BooleanField(default=True)
    info = models.CharField(max_length=300)

#用户信息
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True)
    company = models.ForeignKey(Company)
    role = models.ForeignKey(RoleList)
    is_deleted = models.BooleanField(blank=True, default=False)
