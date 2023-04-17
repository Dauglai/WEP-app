from django.shortcuts import render
from django.views.generic import ListView

from student.models import Account_Statistics


def index(request):
    return render(request, 'main/index.html')


def statistics(request):
    stats = Account_Statistics.objects.order_by('-score').all()
    print(stats)
    data = {
        'stats': stats
    }
    return render(request, "main/rating_table.html", context=data)

class StatisticListView(ListView):
    model = Account_Statistics
    template_name = "main/rating_table.html"


def login(request):
    return render(request, 'registration/login.html')

