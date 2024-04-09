from django.shortcuts import render
from django.http import JsonResponse
from .models import Caso_Model
import requests


def dashboard(request):
    return render(request, 'app_teste/dashboard.html')

