from django.shortcuts import render


def index(request):
    return render(request, 'managerapp/index.html')


def manager(request):
    return render(request, 'managerapp/manager.html')

