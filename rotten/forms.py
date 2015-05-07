
from django.core.exceptions import ObjectDoesNotExist
from django import forms

class SearchForm(forms.Form):
	query = forms.CharField(
	label='Enter anything to search',
	widget=forms.TextInput(attrs={'size': 32})
	)