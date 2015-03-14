from django.shortcuts import render
from census.models import Course,Count,Lesson

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

def cours(request, id_cours):
	course = Course.objects.get(id=id_cours)
	lessons = Lesson.objects.filter(course=course).order_by('number')
	for lesson in lessons:
		lesson.counts = Count.objects.filter(lesson=lesson)
		if (lesson.counts.count() != 0):
			lesson.totalsum = 0 
			for count in lesson.counts:
				count.ratio = round(count.census/lesson.course.enrolled*100)
				lesson.totalsum += count.census
			lesson.totalratio = round(lesson.totalsum/(lesson.counts.count()*course.enrolled)*100)
		else:
			lesson.counts = None
	return render(request, 'coursTemplate.html', {'course' : course, 'lessons' : lessons,})
