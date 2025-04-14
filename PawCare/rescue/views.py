from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,get_object_or_404
from .models import Animal,RescueReport

def animal_list(request):
    animals=Animal.objects.all()
    return render(request,'rescue/animal_list.html',{'animals':animals})

def animal_detail(request,pk):
    animal=get_object_or_404(Animal,pk=pk)
    reports=animal.reports.all()
    return render(request,'rescue/animal_detail.html',{'animal':animal,'reports':reports})


