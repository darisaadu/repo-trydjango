from django.db import models

from django.urls import reverse

# Create your models here.


class MyProduct(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField(null=False, blank=False)
	price = models.DecimalField(decimal_places=2, max_digits=10000)
	summary = models.TextField(null=True, blank=True)
	featured = models.BooleanField(default=True)


	def __str__(self):
		return "{}".format(self.title)



	def get_absolute_url(self):
		return reverse('myfourthapp:myproduct-detail', kwargs={'id':self.id})
