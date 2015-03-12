from django.db import models

# Create your models here.

class Promotion(models.Model):
	number=models.IntegerField("Numéro")

	def __str__(self):
		return "X%s" % (self.number,)
	class Meta:
         verbose_name = "Promotion"

class Amphi(models.Model):
	name=models.CharField("Nom",max_length=60)
	capacity=models.IntegerField("Capacité")

	def __str__(self):
		return "%s" % (self.name,)
	class Meta:
         verbose_name = "Amphithéâtre"

class Course(models.Model):
	name=models.CharField("Nom",max_length=60)
	promotion=models.ForeignKey(Promotion,verbose_name="Promotion")
	enrolled=models.IntegerField("Nombre d'inscrits")

	def __str__(self):
		return "%s (%s)" % (self.name,self.promotion)
	class Meta:
         verbose_name = "Cours"
         verbose_name_plural = "Cours"

class Professor(models.Model):
	name=models.CharField("Nom",max_length=100)

	def __str__(self):
		return "%s" % (self.name,)
	class Meta:
    	 verbose_name = "Professeur"

class Lesson(models.Model):
	course=models.ForeignKey(Course)
	date=models.DateField("Date")
	number=models.IntegerField("Numéro de la séance",blank=True,null=True)
	professor=models.ForeignKey(Professor,verbose_name="Professeur",blank=True,null=True)
	amphi=models.ForeignKey(Amphi,verbose_name="Amphithéâtre")
	title=models.CharField("Titre",max_length=140,blank=True,null=True)

	def __str__(self):
		if ((self.number is not None) & (self.title is not None)):
			return "%s %s : %s (%s,%s)" % (self.course.name,self.number,self.title,self.course.promotion,self.date)
		elif (self.number is not None):
			return "%s %s (%s,%s)" % (self.course.name,self.number,self.course.promotion,self.date)
		elif (self.title is not None):
			return "%s : %s (%s,%s)" % (self.course.name,self.title,self.course.promotion,self.date)
		else:
			return "%s (%s,%s)" % (self.course.name,self.course.promotion,self.date)

	class Meta:
         verbose_name = "Séance"

class Count(models.Model):
	lesson=models.ForeignKey(Lesson,verbose_name="Séance")
	census=models.IntegerField("Nombre d'éléves présents")
	date=models.DateTimeField("Soumis le",auto_now="True")
	comment=models.TextField("Commentaires")
	signature=models.CharField("signature",max_length=120)


	def __str__(self):
		return "%s : %s/%s" % (self.lesson,self.census,self.lesson.course.enrolled)
	class Meta:
         verbose_name = "Comptage"
