# -*- coding: utf-8 -*-
from django import forms
from feedback.models import Feedback

class FeedbackForm(forms.ModelForm):
	
	# Invalid characters
	chars = [";","/","]","[","{","}","=","-","_",")","(","*","&","^","%","$",u"£","`",u"¬",u"¦","\\","|","<",">"]
	
	# Field options
	type_choices = [("0","Select"),("General","General"),("Suggestion","Suggestion"),("Error or Bug","Error or Bug"),("Other", "Other - Explain below")]
	
	# Form fields
	email = forms.EmailField(label = "Email", error_messages = {"required" : "The email field is required."})
	type = forms.ChoiceField(label = "Type", choices = type_choices, widget = forms.Select(), error_messages = {"required" : "Feedback type is required."})
	comment = forms.CharField(max_length = 450, label = "Comment", widget=forms.Textarea(attrs={"style" : "resize:none", "cols" : 46, "rows" : 10}), error_messages = {"required" : "The comment field is required."})
	
	def clean_type(self):
		
		'''
		Field specific method that ensures
		a feedback type was selected.
		'''
		
		type = self.cleaned_data["type"]
		if type == "0" or type == None or not type:
			raise forms.ValidationError("Select a feedback type.")
		return type
	
	class Meta:
		
		'''
		Meta class used to associate the form with the feedback model.
		Exclude provides a list of fields to omit from the form
		'''
		
		model = Feedback
		exclude = ("user", "datetime_posted")
