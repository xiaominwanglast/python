from django.urls import path
from django.conf.urls import url
from task import views_task
from task import views_bug
urlpatterns = [
    path('task/', views_task.Task.as_view()),
    path('bug/', views_bug.Bug.as_view()),
]
