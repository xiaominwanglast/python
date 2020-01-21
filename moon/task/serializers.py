from rest_framework import  serializers
from task.models import *


class Tasksserializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields =("team","project","taskName","taskLink","subTest","oldTestTime","newTestTime",
                "onlineTime","testPerson","taskStatus","tag","importance")


class Bugsserializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    class Meta:
        model = Bugs
        fields = "__all__"