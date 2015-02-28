from django.db import models

# Create your models here.

class Promotion(models.Model):
	number=models.IntegerField("Numéro")

	def __str__(self):
		return "X%s" % (self.number,)

class Amphi(models.Model):
	name=models.CharField("Nom",max_length=60)
	capacity=models.IntegerField("Capacité")

	def __str__(self):
		return "%s" % (self.name,)

class Course(models.Model):
	name=models.CharField("Nom",max_length=6)
	promotion=models.ForeignKey(Promotion)
	enrolled=models.IntegerField("Nombre d'inscrits")

	def __str__(self):
		return "%s (%s)" % (self.name,self.promotion)

class Professor(models.Model):
	name=models.CharField("Nom",max_length=100)

	def __str__(self):
		return "%s" % (self.name,)

class Lesson(models.Model):
	course=models.ForeignKey(Course)
	date=models.DateField("Date")
	number=models.IntegerField("Numéro de la séance")
	professor=models.ForeignKey(Professor)

	def __str__(self):
		return "%s %s (%s,%s)" % (self.course.name,self.number,self.course.promotion,self.date)

class Count(models.Model):
	lesson=models.ForeignKey(Lesson)
	census=models.IntegerField("Nombre d'éléves présents")

	def __str__(self):
		return "%s/%s : %s" % (self.census,self.lesson.course.enrolled,self.lesson)