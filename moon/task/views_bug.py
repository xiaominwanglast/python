from task.models import Bugs
from task.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
import datetime
import calendar

class Bug(generics.GenericAPIView):
    """bug汇总"""
    serializer_class = Bugsserializer

    def get(self,request):
        """获取bug列表"""
        starttime = request.query_params.get("value1")
        endtime = request.query_params.get("value2")
        print (starttime,endtime)
        if starttime=='0':
            myBugResult=Bugs.objects.filter(delete_flag=0).order_by("team")
            serializer=Bugsserializer(myBugResult, many=True)
            return Response({"status":True,"message":"成功","data":serializer.data})
        else:
            if starttime!=endtime:
                myBugResult=Bugs.objects.filter(troubletime__gte=starttime,troubletime__lt=endtime, delete_flag=0).order_by("team")
                serializer=Bugsserializer(myBugResult, many=True)
                return Response({"status":True,"message":"成功","data":serializer.data})
            else:
                years=starttime.split("-")[0]
                month=starttime.split("-")[1]
                days=calendar.monthrange(int(years), int(month))
                starttime = years+"-"+month+"-01"
                endtime   = years+"-"+month+"-"+str(days[1])
                myBugResult=Bugs.objects.filter(troubletime__gte=starttime,troubletime__lte=endtime, delete_flag=0).order_by("team")
                serializer=Bugsserializer(myBugResult, many=True)
                return Response({"status":True,"message":"成功","data":serializer.data})

    def post(self,request):
        """新增bug"""
        request.data["mainside"] = ','.join(request.data["mainside"])
        request.data["otherside"] = ','.join(request.data["otherside"])
        serializer =Bugsserializer(data=request.data)
        if not serializer.is_valid():
            print('序列化不正确')
            return Response({"status": False, "message": "数据格式不正确", "data": serializer.errors})
        serializer.save()
        return Response({"status": True, "message": "新建bug成功", "data": serializer.data})

    def put(self,request):
        """修改bug"""
        myBugResult = Bugs.objects.get(id=request.data['id'], delete_flag=0)
        if not myBugResult:
            return Response({"status":False,"message":"任务名找不到"})
        request.data["mainside"] = ','.join(request.data["mainside"])
        request.data["otherside"] = ','.join(request.data["otherside"])
        # print (request.data)
        serializer = Bugsserializer(myBugResult, data=request.data)
        if not serializer.is_valid():
            print('序列化不正确,不更新数据')
            return Response({"status": False, "message": "数据格式不正确", "data": serializer.errors})
        serializer.save()
        return Response({"status": True, "message": "修改任务成功", "data": serializer.data})

    def delete(self,request):
        """删除bug"""
        myBugResult=Bugs.objects.get(id=int(request.query_params.get('id')), delete_flag=0)
        myBugResult.delete_flag=1
        myBugResult.save()
        return Response({"status": True, "message": "删除任务成功"})
