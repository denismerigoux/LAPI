from django.shortcuts import render
from census.models import Course,Count,Lesson
from django import forms
from django.db.models.aggregates import Max
from datetime import *
from django.http import HttpResponseRedirect

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
	course.lessons = Lesson.objects.filter(course=course,date__lte=datetime.today()).order_by('number')
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
	if (course.nonnulllessonscount != 0):
		course.totalratio = round(course.totalsum / course.nonnulllessonscount)
		course.progressbarclass = getProgressBarClass(course.totalratio)
	else:
		course.totalratio = 0
	course.lessonscount= course.lessons.count()
	return course

class addCountForm(forms.ModelForm):
    class Meta:
        model = Count
    def clean_census(self):
    	census = self.cleaned_data['census']
    	enrolled = self.cleaned_data['lesson'].course.enrolled
    	if (census>enrolled):
        	raise forms.ValidationError("Tu as compté plus de gens qu'il n'y a de personnes inscrites dans ce cours !")
    	return census  # Ne pas oublier de renvoyer le contenu du champ traité

#Views

def home(request):
	#Retrieving the course list and the statistics
	courses = Course.objects.annotate(latest_lesson_date=Max('lesson__date')).filter(latest_lesson_date__lte=datetime.today()).order_by('-latest_lesson_date')
	#courses = Course.objects.all().order_by('-promotion')
	for course in courses:
		course = getCourseStatistics(course)
	#Retrieving last count
	if (Count.objects.all().count() != 0):
		lastcount = Count.objects.latest('date')
		lastcount.ratio = round(lastcount.census/lastcount.lesson.course.enrolled*100)
		lastcount.progressbarclass= getProgressBarClass(lastcount.ratio)
	else:
		lastcount = None

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
        form.fields["lesson"].queryset = Lesson.objects.filter(date__lte=datetime.now(),date__gte=datetime.now()-datetime.timedelta(30)).order_by('-date')
        # check whether it's valid:
        if form.is_valid():
            count = form.save()
            return HttpResponseRedirect('/cours/'+ str(count.lesson.course.id))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = addCountForm()
        form.fields["lesson"].queryset = Lesson.objects.filter(date__lte=datetime.now(),date__gte=datetime.now()-timedelta(30)).order_by('-date') 

    return render(request, 'addcountTemplate.html', {'form': form})
