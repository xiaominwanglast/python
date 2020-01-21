from rest_framework import serializers
from userapp.models import *

class UsersSerializerParam(serializers.Serializer):
    username = serializers.CharField(label="用户名", required=True, max_length=100)
    password = serializers.CharField(label="密码", required=True, max_length=100)

class UsersSerializer(serializers.ModelSerializer):
    color = serializers.ReadOnlyField(source='userscolor.color')
    class Meta:
        model = Users
        fields = ('id', 'username', 'realname', 'email', 'business_group','lastDepartment', 'team', 'group_data','department_list', 'status' ,'color')

class UsersSerializerRealname(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('realname',)

class UsersSerializerNameMail(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username', 'realname', 'email')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields= ('departmentsecond','departmentthird','team')

