from django.urls import path
from . import views

urlpatterns = [

    path('', views.hello_world, name='hello_world'),
    path('helloworld/', views.hello_world2, name='hello_world2'),
#try adding a path in '' helloworld
]