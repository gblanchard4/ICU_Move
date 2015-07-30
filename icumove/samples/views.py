from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.template.defaulttags import register


from itertools import chain

from .models import Air, Stool, Environment

@register.filter
def get_air_day(dictionary, key):
    return dictionary.get(key)[0]

@register.filter
def get_stool_day(dictionary, key):
    return dictionary.get(key)[1]

@register.filter
def get_enviro_day(dictionary, key):
    return dictionary.get(key)[2]  

@register.filter
def get_total_day(dictionary, key):
    return dictionary.get(key)[3]  

# @register.filter
# def get_door_day(dictionary, key):
#     return dictionary.get(key)[2]

# @register.filter
# def get_floor_day(dictionary, key):
#     return dictionary.get(key)[3]  

# @register.filter
# def get_total_day(dictionary, key):
    # return dictionary.get(key)[4]  

# All the samples together
def index(request):

	# Counts
	airs_count = len(Air.objects.all())
	stools_count = len(Stool.objects.all())
	enviro_count = len(Environment.objects.all())
	# doors_count = len(Door.objects.all())
	# floors_count = len(Floor.objects.all())
	# samples_count = airs_count + stools_count + doors_count + floors_count
	samples_count = airs_count + stools_count + enviro_count

	# Dates
	airs_dates = [air.sample_date for air in Air.objects.all()]
	stools_dates = [stool.sample_date for stool in Stool.objects.all()]
	enviro_dates = [enviro.sample_date for enviro in Environment.objects.all()]
	#doors_dates = [door.sample_date for door in Door.objects.all()]
	#floors_dates = [floor.sample_date for floor in Floor.objects.all()]
	#dates = (airs_dates+stools_dates+doors_dates+floors_dates)
	dates = (airs_dates+stools_dates+enviro_dates)
	date_set = sorted(set(dates))

	date_dictionary = {}
	for date in date_set:
		air_on_day = len(Air.objects.filter(sample_date=date))
		stool_on_day = len(Stool.objects.filter(sample_date=date))
		enviro_on_day = len(Environment.objects.filter(sample_date=date))
		#door_on_day = len(Door.objects.filter(sample_date=date))
		#floor_on_day = len(Floor.objects.filter(sample_date=date))
		#total_on_day = (air_on_day+stool_on_day+door_on_day+floor_on_day)
		total_on_day = (air_on_day+stool_on_day+enviro_on_day)
		#date_dictionary[date] = (air_on_day, stool_on_day, door_on_day, floor_on_day, total_on_day)
		date_dictionary[date] = (air_on_day, stool_on_day, enviro_on_day, total_on_day)
								 

	template = 'samples/index.html'
	#context = {'samples':samples_count, 'airs':airs_count, 'stools':stools_count, 'doors':doors_count, 'floors':floors_count, 'date_set':date_set, 'date_dictionary':date_dictionary}
	context = {'samples':samples_count, 'airs':airs_count, 'stools':stools_count, 'enviros':enviro_count, 'date_set':date_set, 'date_dictionary':date_dictionary}

	return render(request, template, context)

def date_view(request, date):
	print date
	airs = Air.objects.filter(sample_date=date)
	stools = Stool.objects.filter(sample_date=date)
	# doors = Door.objects.filter(sample_date=date)
	# floors = Floor.objects.filter(sample_date=date)

	template = 'samples/dates.html'
	#context={'date':date, 'airs':airs, 'stools':stools, 'doors':doors, 'floors':floors }
	context={'date':date, 'airs':airs, 'stools':stools}

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

	
# def door_index(request):
# 	doors_list = Door.objects.order_by('sample_date')
	
# 	template = 'samples/doors.html'
# 	context = {'doors_list':doors_list}

# 	return render(request, template, context)

# def door_detail(request, uid):
# 	door = get_object_or_404(Door, pk=uid)

# 	template = 'samples/door_detail.html'

# 	return render(request, template, {'door':door})
	
# def floor_index(request):
# 	floors_list = Floor.objects.order_by('sample_date')

# 	template = 'samples/floors.html'
# 	context = {'floors_list':floors_list}

# 	return render(request, template, context)

# def floor_detail(request, uid):
# 	floor = get_object_or_404(Floor, pk=uid)

# 	template = 'samples/floor_detail.html'

# 	return render(request, template, {'floor':floor})
