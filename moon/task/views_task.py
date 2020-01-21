from task.models import Tasks
from task.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

class Task(generics.GenericAPIView):
    """
    任务
    """
    serializer_class = Tasksserializer
    def get(self,request):
        """获取任务列表"""

        taskList=Tasks.objects.filter(delete_flag=0).order_by("team","project","taskName")
        serializer=Tasksserializer(taskList, many=True)
        return Response({'status':True,"message":"成功","data":serializer.data})

    def post(self,request):
        """新建任务列表"""
        if request.data["newTestTime"]==[]:
            request.data["newTestTime"]=request.data["oldTestTime"]
        request.data["oldTestTime"]=','.join([str(i) for i in request.data["oldTestTime"]])
        request.data["newTestTime"] = ','.join([str(i) for i in request.data["newTestTime"]])
        request.data["testPerson"] = ','.join(request.data["testPerson"])
        serializer = Tasksserializer(data=request.data)
        if not serializer.is_valid():
            print('序列化不正确')
            return Response({"status": False, "message": "数据格式不正确", "data": serializer.errors})
        serializer.save()
        return Response({"status": True, "message": "新建任务成功", "data": serializer.data})

    def put(self,request):
        """修改任务列表"""
        myTaskResult = Tasks.objects.get(taskName=request.data["taskName"],delete_flag=0)
        if not myTaskResult:
            return Response({"status":False,"message":"任务名找不到"})
        if request.data["newTestTime"]==[]:
            request.data["newTestTime"]=request.data["oldTestTime"]
        request.data["oldTestTime"]=','.join([str(i) for i in request.data["oldTestTime"]])
        request.data["newTestTime"] = ','.join([str(i) for i in request.data["newTestTime"]])
        request.data["testPerson"] = ','.join(request.data["testPerson"])
        serializer = Tasksserializer(myTaskResult, data=request.data)
        if not serializer.is_valid():
            print('序列化不正确,不更新数据')
            return Response({"status": False, "message": "数据格式不正确", "data": serializer.errors})
        serializer.save()
        return Response({"status": True, "message": "修改任务成功", "data": serializer.data})

    def delete(self,request):
        """删除任务"""
        myTaskResult=Tasks.objects.get(taskName=request.query_params.get["taskName"],delete_flag=0)
        myTaskResult["delete_flag"]=1
        myTaskResult.save()
        return Response({"status": True, "message": "删除任务成功"})
