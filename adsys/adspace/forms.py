# -*- coding: utf-8 -*-
from django import forms
from adspace.models import AdSpace

class AdSpaceForm(forms.Form):
	
	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		super(AdSpaceForm, self).__init__(*args, **kwargs)
	
	# List of invalid characters
	chars = [";","/","]","[","{","}","=","-","_",")","(","*","&","^","%","$",u"£","`",u"¬",u"¦","\\","|","<",">"]
	
	# Form field options
	size_choices = [("1","320 x 400"), ("2","430 x 300"), ("3","250 x 515")]
	colour_choices = [("#000000","Black"),("#FF0000", "Red"),("#006400", "Dark Green"),("#0000FF", "Blue")]
	
	# Form fields
	title = forms.CharField(label = "Title:", max_length = 80, error_messages = {"required" : "AdSpaces require a title."})
	adspace_size = forms.ChoiceField(label = "AdSpace size (in pixels)", choices = size_choices, widget=forms.RadioSelect(), error_messages = {"required" : "AdSpaces require a size."})
	adspace_border_colour = forms.ChoiceField(label = "Border colour", choices = colour_choices, widget=forms.Select(), error_messages = {"required" : "AdSpaces require a border color."})
	
	def clean_title(self):
		
		'''
		Form field specific function that validates the adspace title.
		Checks for invalid characters, title length and whether the
		adspace title already exists for that user.
		'''
		
		title = self.cleaned_data["title"]
		for char in self.chars:
			if char in title:
				raise forms.ValidationError("Title contains invalid characters. Only !, ?, ,, @, ', :, +, #, are allowed.")
		title = title.strip()
		if len(title) < 10:
			raise forms.ValidationError("Title is too short. Must be at least 10 characters long.")
		elif len(title) > 80:
			raise forms.ValidationError("Title is too long.")
		
		title_count = AdSpace.objects.filter(user = self.request.user, title__iexact = title).count()
		if title_count == 1:
			raise forms.ValidationError("You have already created an AdSpace with the same title. Please choose another.")
		
		return title

class DeleteAdSpaceForm(forms.ModelForm):
	
	'''
	Form class managing the delete adspace functionality
	It is a model form so the model field in the Meta class
	is referenced to AdSpace
	'''
	class Meta:
		model = AdSpace
		fields = []