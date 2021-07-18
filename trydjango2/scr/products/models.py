from django.db import models
from django.urls import reverse

class Product(models.Model):
	title 		= models.CharField(max_length=150)
	description = models.TextField(blank=True, null=True)
	price 		= models.DecimalField(decimal_places=2, max_digits=1000, blank=True, null=True)
	summary 	= models.TextField(blank=True, null=True)
	featured 	= models.BooleanField(default=True)


	def get_absolute_url(self):
		return reverse("products:product-detail", kwargs={'id': self.id})
		#f"/product/{self.id}/"


	def __str__(self):
		return self.title  