from django.db import models

class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.CharField('四级部门',max_length=100,blank=True)
    project = models.CharField("项目名称-大类",max_length=100,blank=True)
    taskName = models.CharField("任务名称",max_length=100,blank=True)
    taskLink = models.CharField("任务链接",max_length=100,blank=True)
    subTest = models.CharField("提测时间",max_length=100,blank=True)
    oldTestTime =models.CharField("原测试时间",max_length=100,blank=True)
    newTestTime = models.CharField("调整后测试时间", max_length=100, blank=True)
    onlineTime = models.CharField("上线时间", max_length=100, blank=True)
    testPerson = models.CharField("测试人员", max_length=100, blank=True)
    taskStatus = models.CharField("任务状态", max_length=100, blank=True)
    tag = models.CharField("备注", max_length=500, blank=True)
    importance =models.CharField("是否重点任务，0是非重点，1是重点", max_length=1,default='0')
    delete_flag = models.CharField("是否删除，0是非删除，1是删除", max_length=1, default='0')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)


class Bugs(models.Model):
    id = models.AutoField(primary_key=True)
    team =models.CharField("四级部门",max_length=100,blank=True)
    project =models.CharField("项目",max_length=100,blank=True)
    troubletype = models.CharField("事故定级",max_length=100,blank=True)
    troubledesc = models.CharField("问题描述",max_length=1000,blank=True)
    mainside = models.CharField("主责方",max_length=100,blank=True)
    otherside = models.CharField("次责方",max_length=100,blank=True)
    troubletime = models.CharField("事故时间",max_length=100,blank=True)
    effacttime = models.CharField("线上影响时间", max_length=100, blank=True)
    effactusercnt = models.CharField("影响用户量", max_length=100, blank=True)
    effactmoney = models.CharField("影响金额", max_length=100, blank=True)
    delete_flag = models.CharField("是否删除，0是非删除，1是删除", max_length=1, default='0')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)