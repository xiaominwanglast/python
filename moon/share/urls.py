from django.urls import path
from django.conf.urls import url
from share import views
urlpatterns = [
    path('shares/',views.Shares.as_view()),
    path('shares/check/',views.ShareCheck.as_view())
]
