from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('upload', views.upload, name='upload'),
    path('download', views.download, name='download'),
    path('code', views.code_page, name='code'),
]
