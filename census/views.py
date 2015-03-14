from django.shortcuts import render
from census.models import Course,Count,Lesson
from django import forms

#Auxiliariy functions

def getProgressBarClass(ratio):
	if (ratio > 75):
		return "success"
	elif (ratio > 50):
		return "info"
	elif (ratio > 25):
		return "warning"
	else:
		return "danger"

def getCourseStatistics(course):
	course.lessons = Lesson.objects.filter(course=course).order_by('number')
	course.totalsum = 0
	course.nonnulllessonscount = 0
	for lesson in course.lessons:
		lesson.counts = Count.objects.filter(lesson=lesson)
		if (lesson.counts.count() != 0):
			lesson.totalsum = 0 
			for count in lesson.counts:
				count.ratio = round(count.census/lesson.course.enrolled*100)
				lesson.totalsum += count.census
			lesson.totalratio = round(lesson.totalsum/(lesson.counts.count()*course.enrolled)*100)
			lesson.progressbarclass = getProgressBarClass(lesson.totalratio)
			course.totalsum += lesson.totalratio
			course.nonnulllessonscount += 1
		else:
			lesson.counts = None
	if (course.lessons.count() != 0):
		course.totalratio = round(course.totalsum / course.nonnulllessonscount)
		course.progressbarclass = getProgressBarClass(course.totalratio)
	else:
		course.totalratio = 0
	course.lessonscount= course.lessons.count()
	return course

class addCountForm(forms.Form):
	course = forms.CharField(label="Cours",max_length=60)

#Views

def home(request):
	#Retrieving the course list and the statistics
	courses = Course.objects.filter(promotion__number=2014)
	for course in courses:
		course = getCourseStatistics(course)
	#Retrieving last count
	lastcount = Count.objects.latest('date')
	lastcount.ratio = round(lastcount.census/lastcount.lesson.course.enrolled*100)
	lastcount.progressbarclass= getProgressBarClass(lastcount.ratio)

	return render(request,'homeTemplate.html', {'courses' : courses, 'lastcount' : lastcount,})

def comptage(request):
	return render(request,'comptageTemplate.html')

def cours(request, id_cours):
	course = Course.objects.get(id=id_cours)
	course = getCourseStatistics(course)
	return render(request, 'coursTemplate.html', {'course' : course,})

def addcount(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = addCountForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = addCountForm()

    return render(request, 'addcountTemplate.html', {'form': form})
