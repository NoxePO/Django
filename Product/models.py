from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Products(models.Model):
	name = models.CharField(max_length = 50)
	count = models.CharField(max_length = 3)
	def __str__ (self):
		return self.name
	#property
	def fullname(self):
		return self.name + "[" + self.count + "]"		
	def get_reverse_url(self):
		return reverse("prod_new", kwgs = {"id": self.id})
	def get_reverse_url(self):
		return reverse("prod_edit", kwgs = {"id": self.id})
	def get_reverse_url(self):
		return reverse("prod_delete", kwgs = {"id": self.id})

class Orders(models.Model):
	orderName = models.CharField(max_length = 50)
	startDate = models.DateField()
	stopDate = models.DateField()
	item = models.ForeignKey(Products, related_name = "Products")
	def __str__ (self):
		return self.orderName
	def get_reverse_url(self):
		return reverse("order_new", kwgs = {"id": self.id})
	def get_reverse_url(self):
		return reverse("order_edit", kwgs = {"id": self.id})
	def get_reverse_url(self):
		return reverse("order_delete", kwgs = {"id": self.id})


class Workers(models.Model):
	name = models.CharField(max_length = 50)
	forename = models.CharField(max_length = 50)
	orderid = models.ForeignKey(Orders, related_name = "Orders")
	def __str__ (self):
		return self.forename
	def get_reverse_url(self):
		return reverse("worker_new", kwgs = {"id": self.id})
	def get_reverse_url(self):
		return reverse("worker_edit", kwgs = {"id": self.id})
	def get_reverse_url(self):
		return reverse("worker_delete", kwgs = {"id": self.id})
