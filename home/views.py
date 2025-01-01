from django.shortcuts import render, redirect,get_object_or_404, redirect
from .models import Resource

def list(request):
    resources = Resource.objects.all()
    return render(request, 'list.html', {'resources': resources})


        
  
def home(request):   
    return render(request, 'home.html')
