from django.shortcuts import render
from django.http import HttpResponse

def office(request):
    return render(request, 'frontMain/teacher.html')
