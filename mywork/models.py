from __future__ import unicode_literals

from django.db import models
#from .models import mywork
#admin.site.register(mywork)

# Create your models here.

#class Person(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#    def __unicode__ (self):
#        return self.first_name
#    def __str__ (self):
#        return self.first_name
#####################################################
class orashipping(models.Model):
	datetime = models.DateField()
	management = models.CharField(max_length= 30)
	consignee = models.CharField(max_length=30)
	objective = models.CharField(max_length=30)
	name_emp = models.CharField(max_length=30)
	driver_man = models.CharField(max_length=30)
	no_car = models.CharField(max_length=30)
	totel = models.CharField(max_length=30)
	type_no = models.CharField(max_length=30)
	Specifications = models.CharField(max_length=30)
	Notes = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.objective
		pass#

	def __str__(self):
		return self.objective
		pass
