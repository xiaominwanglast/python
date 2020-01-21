from django.db import models

# Create your models here.

class Share(models.Model):
    id = models.AutoField(primary_key=True)
    team =models.CharField("四级部门名",max_length=100,blank=True)
    shareperson = models.CharField("分享人",max_length=100,blank=True)
    sharetime =models.CharField("分享时间",max_length=100,blank=True)
    sharetitle =models.CharField("分享主题",max_length=100,blank=True)
    shareaddress = models.CharField("分享地址",max_length=100,blank=True)
    delete_flag = models.CharField("是否删除，0是非删除，1是删除", max_length=1, default='0')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)