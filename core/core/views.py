from django.shortcuts import render
from projects.models import Project
from clients.models import Client

def landing_page(request):
    projects = Project.objects.all()
    clients = Client.objects.all()
    return render(request, 'landing.html', {
        'projects': projects,
        'clients': clients
    })
