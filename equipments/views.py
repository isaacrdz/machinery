from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Equipment
from models import *



def equipment_view(request, model):
	equipment = get_object_or_404(Equipment, model = model)
	template = 'equipos.html'
	return render(request,template,{'equipment':equipment,})

def home  (request):
	equipment = Equipment.objects.all()
	family = Family.objects.all()
	template = 'equipos-dos.html'
	return render(request,template,{'equipment':equipment, 'family':family, 'request':request})
	

# Create your views here.
