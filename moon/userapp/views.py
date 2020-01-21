from userapp.models import Users
from userapp.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from userapp.ldapcore import *
import re
import json

class UserAuth(generics.GenericAPIView):
    """
    用户登录鉴权
    """
    # 配合文档，显示请求参数
    serializer_class = UsersSerializerParam

    def get(self, request):
        """
        判断用户session是否过期
        """
        try:
            user = request.session['user']
            serializer = UsersSerializer(user)
            return Response({"status": True, "message": "成功", "data": serializer.data})
        except:
            return Response({"status": False, "message": "失败"})

    def post(self, request):
        """
        用户登录鉴权，域账号登录
        """
        username = request.data.get('username')
        password = request.data.get('password')
        # ldap验证身份
        ldap = ADUtil()
        ldap_user = ldap.auth(username, password)
        if ldap_user[0] != 'OK':
            return Response({"status": False, "message": "登录失败，身份验证出错", "data": ""})
        # 创建用户
        userinfo, created = Users.objects.get_or_create(username=username)
        if created:
            userinfo.realname = str(ldap_user[2]['displayName'], encoding='utf-8')
            userinfo.email = str(ldap_user[2]['mail'], encoding='utf-8')
        userinfo.group_data = str(ldap_user[2]['distinguishedName'], encoding='utf-8')
        group_data = re.findall("OU=(.*?),", userinfo.group_data, re.I)
        userinfo.business_group = group_data[-2]
        userinfo.team = group_data[0]
        userinfo.lastDepartment = group_data[1]
        userinfo.department_list = json.dumps(group_data[:-1][::-1], ensure_ascii=False)
        userinfo.save()

        #创建颜色
        usercolor,created = UsersColor.objects.get_or_create(color = '#007500', users=userinfo)
        if created:
            usercolor.save()

        #创建新组
        groups,created = Groups.objects.get_or_create(lastDepartment=group_data[1],team=group_data[0])
        if created:
            groups.save()

        serializer = UsersSerializer(userinfo)
        # 设置session
        request.session['user'] = serializer.data
        print (serializer.data)
        return Response({"status": True, "message": "成功", "data": serializer.data})

    def delete(self, request):
        """
        用户退出登录
        """
        del request.session['user']
        return Response({"status": True, "message": "成功", "data": {}})


class UserList(generics.GenericAPIView):
    """
    用户列表
    """

    # 配合文档，显示请求参数
    serializer_class = UsersSerializerParam

    def get(self, request):
        """
        获取级别部门下所有用户列表
        """

        users = Users.objects.filter(departmentthird=request.query_params.get('departmentthird'))
        serializer = UsersSerializerRealname(users, many=True)
        return Response({"status": True, "message": "成功", "data": serializer.data})

class GroupList(generics.GenericAPIView):
    """
    获取四级部门信息
    """

    serializer_class = GroupSerializer

    def get(self,request):
        """
        获取四级部门信息
        :return:
        """

        groups = Groups.objects.filter(departmentthird=request.query_params.get('departmentthird'))
        serializer = GroupSerializer(groups, many=True)
        return Response({"status": True, "message": "成功", "data": serializer.data})
