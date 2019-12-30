from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from adoption import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^adoptions/(\d+)/', views.pet_detail, name='pet_detail'),
]
