from django.shortcuts import render

from html_template.models import Service

# Create your views here.

def template(request):
    services = Service.objects.all()
    return render(request, 'index.html',context={'services':services})