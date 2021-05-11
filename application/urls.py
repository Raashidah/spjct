
from django.urls import path,include
from . import views

urlpatterns = [
    path('one',views.fun1,name='one')
]