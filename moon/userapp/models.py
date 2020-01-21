from django.db import models


class Users(models.Model):
    """ 用户信息表 """
    id = models.AutoField(primary_key=True)
    username = models.CharField('用户登录名', max_length=100)
    realname = models.CharField('真实姓名', max_length=100, blank=True, )
    email = models.TextField('邮箱', blank=True, default='')
    business_group = models.CharField('事业群', max_length=100, blank=True, )
    lastDepartment = models.CharField('上级部门', max_length=100, blank=True, )
    team = models.CharField('团队', max_length=100, blank=True, )
    group_data = models.CharField('部门具体信息原始数据', max_length=500, blank=True, )
    department_list = models.CharField('部门层级列表', max_length=500, blank=True, )
    status = models.CharField('状态', blank=True, max_length=100, default='1')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.id, self.username, self.realname


class UsersColor(models.Model):
    """用户颜色表"""
    id = models.AutoField(primary_key=True)
    color = models.CharField('颜色',max_length=30,blank=True, )
    users = models.OneToOneField(Users,on_delete=models.CASCADE)

    def __str__(self):
        return self.id, self.color


class Groups(models.Model):
    """获取组信息"""
    id = models.AutoField(primary_key=True)
    lastDepartment = models.CharField('三级部门',max_length=100,blank=True)
    team = models.CharField('四级部门',max_length=100,blank=True)


