from django.shortcuts import render
from census.models import Course,Count

# Create your views here.

def home(request):
	#Retrieving the course list
	courses = Course.objects.filter(promotion__number=2014)
	#Retrieving last count
	lastcount = Count.objects.latest('lesson__date')
	lastcountratio = round(lastcount.census/lastcount.lesson.course.enrolled*100)
	
	return render(request,'homeTemplate.html', {'courses' : courses, 'lastcount' : lastcount, 'lastcountratio' : lastcountratio})

def comptage(request):
	return render(request,'comptageTemplate.html')
