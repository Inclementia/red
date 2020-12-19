from django.shortcuts import render

from managerapp.models import Managers

def index(request):
    return render(request, 'managerapp/index.html')


def manager(request):
    managers = Managers.objects.all()
    context = {
        'managers': managers,
        'page_title': 'список'
    }
    return render(request, 'managerapp/manager.html', context)


