from django.urls import path
from .import  views
urlpatterns=[
    path('<str:rf_id>/', views.validation, name='validation'),
]
