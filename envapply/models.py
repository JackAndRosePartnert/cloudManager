#coding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Env(models.Model):
    env_name=models.CharField(max_length=50)
    env_type=models.CharField(max_length=10) #开发环境类型A类型，B类型，C类型
    vm_create_time=models.DateTimeField()
    vm_state=models.CharField(max_length=10) #0创建中，1创建失败，2创建成功，3正常运行 4关机

#开发环境申请审批表
class EnvApplyApprove(models.Model):
    apply_user = models.ForeignKey(User,related_name='applyuser') #用户和申请审批表一对多，将user作为外键
    apply_env = models.ForeignKey(Env) #开发环境和表一对一
    apply_time = models.DateTimeField()
    status = models.CharField(max_length=10)# 0 未处理 1拒绝   2通过 好处：不需要同步申请和审批状态
    approve_user = models.ForeignKey(User,related_name='approveuser')
    approve_time = models.DateTimeField(blank=True)
    operate = models.CharField(max_length=50) #管理员可以执行的操作
    env_name = models.CharField(max_length=50,default="")
