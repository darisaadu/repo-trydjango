from django.db import models

from django.urls import reverse

# Create your models here.

class Course(models.Model):
	title = models.CharField(max_length=120)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		# return reverse(['courses','course-detail'], args=self.id)
		return reverse('courses:course-detail', kwargs={'id': self.id})
