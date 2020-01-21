from django.urls import path
from django.conf.urls import url
from userapp import views

urlpatterns = [
    url(r'^session/$', views.UserAuth.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/groups/', views.GroupList.as_view()),

]
