from django.db import models

# Create your models here.
<<<<<<< Updated upstream

class Course(models.Model):
	name = models.CharField(max_length=128)
	venue = models.CharField(max_length=64)
	subject = models.CharField(max_length=64)
	date = models.DateField('date presented')
	
	def __str__(self):
		title = 'Name: %s' % (self.name)
		title += ' - Venue: %s ' % (self.venue)
		return title
		
class Slides(models.Model):
	session = models.CharField(max_length=128)
	keynote = models.URLField(max_length=256)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.session
=======
>>>>>>> Stashed changes
