from django.shortcuts import render
from rest_framework import viewsets


def index(request):
    return render(request, "index.html")
