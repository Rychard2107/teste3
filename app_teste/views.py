from django.shortcuts import render
from django.http import JsonResponse
from .models import Caso_Model
import requests


def index(request):
    return render(request, 'index.html')

