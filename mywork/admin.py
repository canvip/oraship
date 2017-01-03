from django.contrib import admin

# Register your models here.
from form import   v_orashipping
from .models import   orashipping , Employee, Job #, Person class orashipping


#class PersonModelAdmin(admin.ModelAdmin):
#	search_fields = ["first_name","last_name"]#

#	class meta:
#		model = Person


class OrashippingModelAdmin(admin.ModelAdmin):

	
	search_fields = ["objective","datetime","consignee","type_no"]
	list_display = ["__unicode__","datetime","type_no"]
	list_display_links = ["__unicode__", "datetime","type_no"]
	form = v_orashipping
	list_filter =['consignee',"datetime"]
    
	#class meta:
#		model = orashipping

	



class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'salary')
    list_filter = ['hire_date']
    search_fields = ['last_name']
    date_hierarchy = 'hire_date'

admin.site.register(orashipping,OrashippingModelAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Job)



