
from django import forms
from .models import orashipping
from django.forms import ModelForm


class v_orashipping (forms.ModelForm):
	"""docstring for Orashipping"""
	class meta:
		model = orashipping
		fields = ['type_no']
			
	