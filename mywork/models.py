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




class Job(models.Model):
    job_id = models.CharField(max_length=10, primary_key=True)
    job_title = models.CharField(max_length=35)
    min_salary = models.IntegerField(null=True, blank=True)
    max_salary = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'jobs'
    def __str__(self):
        return self.job_title

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=25)
    email = models.CharField(unique=True, max_length=25)
    phone_number = models.CharField(max_length=20, blank=True)
    hire_date = models.DateField()
    job = models.ForeignKey(Job)
    salary = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    commission_pct = models.DecimalField(null=True, max_digits=2, decimal_places=2, blank=True)
    manager = models.ForeignKey('self', null=True, blank=True)
    department_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'employees'
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)#

#class JobHistory(models.Model):
#    employee = models.ForeignKey(Employee, primary_key=True)
#    start_date = models.DateField(unique=True)
#    end_date = models.DateField()
#    job = models.ForeignKey(Job)
#    department_id = models.IntegerField(null=True, blank=True)
#    class Meta:
#        db_table = u'job_history'
#		