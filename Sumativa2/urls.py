"""Sumativa2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from App1.views import ProductoList, ProductoDetail, CategoriaList, CategoriaDetail
from App2.views import producto_list, producto_detail, categoria_list, categoria_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('producto/cbv/', ProductoList.as_view()),
    path('producto/cbv/<int:pk>', ProductoDetail.as_view()),
    path('categoria/cbv/', CategoriaList.as_view()),
    path('categoria/cbv/<str:pk>', CategoriaDetail.as_view()),
    path('producto/fbv/', producto_list),
    path('producto/fbv/<int:pk>', producto_detail),
    path('categoria/fbv/', categoria_list),
    path('categoria/fbv/<str:pk>', categoria_detail),
]
