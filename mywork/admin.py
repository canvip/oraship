from django.contrib import admin

# Register your models here.
from forms import   v_orashipping
from .models import   orashipping


class OrashippingModelAdmin(admin.ModelAdmin):

	
	search_fields = ["objective","datetime","consignee","type_no"]
	list_display = ["__unicode__","datetime","type_no"]
	list_display_links = ["__unicode__", "datetime","type_no"]
	form = v_orashipping
	list_filter =['consignee',"datetime"]
    
	#class meta:
#		model = orashipping

	




admin.site.register(orashipping,OrashippingModelAdmin)
#admin.site.register(Employee,EmployeeAdmin)
#admin.site.register(Job)



