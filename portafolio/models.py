from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	image = models.ImageField(upload_to='portafolio/images')
	url = models.URLField(max_length=200, blank=True)

	def __str__(self):
		return self.title
