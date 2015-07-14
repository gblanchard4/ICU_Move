from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from itertools import chain

from .models import Air, Stool, Door, Floor

# Create your views here.


# All the samples together
def index(request):
	airs_list = Air.objects.order_by('sample_date')
	stools_list = Stool.objects.order_by('sample_date')
	doors_list = Door.objects.order_by('sample_date')
	floors_list = Floor.objects.order_by('sample_date')
	samples_list = list(chain(airs_list, stools_list, doors_list, floors_list))

	template = 'samples/index.html'
	context = {'samples_list':samples_list, 'airs_list':airs_list, 'stools_list':stools_list, 'doors_list':doors_list, 'floors_list':floors_list}

	return render(request, template, context)

def air_index(request):
	airs_list = Air.objects.order_by('sample_date')
	template = 'samples/airs.html'
	context = {'airs_list':airs_list}
	return render(request, template, context)

def air_detail(request, uid):
	air = get_object_or_404(Air, pk=uid)
	template = 'samples/air_detail.html'
	return render(request, template, {'air':air})

def stool_index(request):
	stools_list = Stool.objects.order_by('sample_date')
	template = 'samples/stools.html'
	context = {'stools_list':stools_list}
	return render(request, template, context)

def stool_detail(request, uid):
	stool = get_object_or_404(Stool, pk=uid)
	template = 'samples/stool_detail.html'
	return render(request, template, {'stool':stool})

	
def door_index(request):
	doors_list = Door.objects.order_by('sample_date')
	
	template = 'samples/doors.html'
	context = {'doors_list':doors_list}

	return render(request, template, context)

def door_detail(request, uid):
	door = get_object_or_404(Door, pk=uid)

	template = 'samples/door_detail.html'

	return render(request, template, {'door':door})
	
def floor_index(request):
	floors_list = Floor.objects.order_by('sample_date')

	template = 'samples/floors.html'
	context = {'floors_list':floors_list}

	return render(request, template, context)

def floor_detail(request, uid):
	floor = get_object_or_404(Floor, pk=uid)

	template = 'samples/floor_detail.html'

	return render(request, template, {'floor':floor})
