from django import forms
from .models import orashipping


class v_orashipping (forms.ModelForm):
	"""docstring for Orashipping"""
	class meta:
		model = orashipping
		fields = ['type_no']
			
	