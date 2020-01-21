from share.models import Share
from share.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class Shares(generics.GenericAPIView):
    """
    分享
    """
    serializer_class = Shareserializers
    def get(self,request):
        """获取分享列表"""
        shareList=Share.objects.filter(delete_flag=0).order_by('team','shareperson')
        serializer=Shareserializers(shareList, many=True)
        return Response({'status':True,"message":"成功","data":serializer.data})

    def post(self,request):
        """新建分享列表"""
        if request.data["sharetitle"]=="":
            return Response({"status": True, "message": "不新建分享", "data": request.data})
        request.data["shareperson"] = ','.join(request.data["shareperson"])
        serializer = Shareserializers(data=request.data)
        if not serializer.is_valid():
            print('序列化不正确')
            return Response({"status": False, "message": "数据格式不正确", "data": serializer.errors})
        serializer.save()
        return Response({"status": True, "message": "新建分享成功", "data": serializer.data})

    def put(self,request):
        """修改分享列表"""
        myShareResult = Share.objects.get(sharetitle=request.data["sharetitle"],delete_flag=0)
        if not myShareResult:
            return Response({"status":False,"message":"分享找不到"})
        request.data["shareperson"] = ','.join(request.data["shareperson"])
        serializer = Shareserializers(myShareResult, data=request.data)
        if not serializer.is_valid():
            print('序列化不正确,不更新数据')
            return Response({"status": False, "message": "数据格式不正确", "data": serializer.errors})
        serializer.save()
        return Response({"status": True, "message": "修改分享成功", "data": serializer.data})

    def delete(self,request):
        """删除分享"""
        myShareResult=Share.objects.get(sharetitle=request.query_params.get("sharetitle"),delete_flag=0)
        myShareResult.delete_flag=1
        myShareResult.save()
        return Response({"status": True, "message": "删除分享成功"})


class ShareCheck(generics.GenericAPIView):
    """检查"""
    serializer_class = Shareserializers

    def get(self,request):
        """获取分享主题"""
        shareList=Share.objects.filter(sharetitle=request.query_params.get("sharetitle"),delete_flag=0)
        if len(shareList)==0:
            return Response({'status':False,"message":"无数据"})
        else:
            return Response({'status':True,"message":"有数据"})
