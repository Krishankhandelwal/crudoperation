from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('create/',create),
    path('',list),
    path('detail/<id>/',detail),
    path('<int:pk>/',update_view),
    path('delete/<int:id>',delete),
]
