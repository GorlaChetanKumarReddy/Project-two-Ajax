"""Project4Ajax URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView,View

from app1 import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='showIndex.html')),
    path('Check_User_Name_Ajax/',views.Check_User_Name_Ajax,name='Check_User_Name_Ajax'),
    path('save_user/',views.save_user,name='save_user'),
]
