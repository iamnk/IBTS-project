from django.urls import path
from .import  views
urlpatterns=[
    path('<str:reg_no>/', views.validation, name='validation'),
]
