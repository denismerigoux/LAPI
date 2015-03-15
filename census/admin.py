from django.contrib import admin
from census.models import *

class CountAdmin(admin.ModelAdmin):
	ordering = ('-date', )

class LessonAdmin(admin.ModelAdmin):
	ordering = ('-date', )

class CourseAdmin(admin.ModelAdmin):
	ordering = ('-promotion', 'name')

# Register your models here.
admin.site.register(Promotion)
admin.site.register(Amphi)
admin.site.register(Course,CourseAdmin)
admin.site.register(Professor)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Count,CountAdmin)
