from django.urls import path
from app_teste.views import index

urlpatterns = [
    path('', index, name='index'),
]
