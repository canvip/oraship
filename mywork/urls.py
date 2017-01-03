from django.conf.urls import url
from .models import orashipping



from .views import (
	create,
	detail,
	list,
	update,
	delete,
	index,
	about,
	)




info_dict = {
     'queryset': orashipping.objects.all(),
     
}
employee_info = {'model' : orashipping}







urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'create^$', create, name='create'),
    url(r'detail$', detail, name='detail'),
    url(r'list$', list, name='list'),
    url(r'update$', update, name='update'),
    url(r'delete$', delete, name='delete'),
    url(r'about$', about, name='about'),

    
]

#


