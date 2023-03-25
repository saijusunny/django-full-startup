from django import views
from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gall', views.gall, name='gall'),
    path('abt', views.abt, name='abt'),
    path('cnt', views.cnt, name='cnt'),
]