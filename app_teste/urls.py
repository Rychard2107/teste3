from django.urls import path
from app_teste.views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]
