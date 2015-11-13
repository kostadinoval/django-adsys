# -*- coding: utf-8 -*-
from django import forms
from advert.models import Advert, AdvertKeyword

class AdvertForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		
		self.request = kwargs.pop('request', None)
		self.edit = kwargs.pop('edit', False)
		self.advert_id = kwargs.pop('advert_id', None)
		super(AdvertForm, self).__init__(*args, **kwargs)
	
	# Invalid characters
	chars = [";","/","]","[","{","}","=","-","_",")","(","*","&","^","%","$",u"£","`",u"¬",u"¦","\\","|","<",">",]
	
	# Form fields
	title = forms.CharField(max_length=80, label = "Title", widget=forms.TextInput(attrs={'placeholder' : 'New online service!'}), error_messages={'required' : 'Advert title cannot be blank.'})
	description = forms.CharField(max_length=300, widget=forms.Textarea(attrs={'style' : 'resize:none', 'cols' : 37, 'rows' : 8, 'placeholder' : 'This is an example of an advert description. It is used to provide a brief description about the advert and what it is about.'}), label = "Description", error_messages={'required' : 'Advert description cannot be blank.'})
	destination_url = forms.URLField(label = "Destination URL", widget=forms.URLInput(attrs={'placeholder' : 'http://www.example.com'}), error_messages={'required' : 'Advert destination URL cannot be blank.'})
	
	def clean_title(self):
		
		'''
		Form field specific function that validates the advert title.
		Checks for invalid characters, title length.
		Checks for adverts with the same title.
		No error is raised if the advert title doesn't change.
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
		
		if self.edit == True:
			title_count = Advert.objects.filter(pk = self.advert_id, user = self.request.user, title__iexact = title).count()
			if title_count == 1:
				return title
			elif title_count == 0:
				title_count = Advert.objects.filter(user = self.request.user, title__iexact = title).count()
				if title_count == 1:
					raise forms.ValidationError("You have already created an advert with the same title. Please choose another.")
		else:
			title_count = Advert.objects.filter(user = self.request.user, title__iexact = title).count()
			if title_count == 1:
				raise forms.ValidationError("You have already created an advert with the same title. Please choose another.")
		
		return title
	
	def clean_description(self):
		
		'''
		Form field specific function that validates the advert description.
		Checks for invalid characters, description length.
		'''
		
		description = self.cleaned_data["description"]
		for char in self.chars:
			if char in description:
				raise forms.ValidationError("Description contains invalid characters. Only !, ?, ,, @, ', :, +, #, are allowed.")
		description = description.strip()
		if len(description) < 150:
			raise forms.ValidationError("Description is too short. Must be at least 150 characters long.")
		elif len(description) > 300:
			raise forms.ValidationError("Description is too long.")
		
		return description
	
	class Meta:
		
		'''
		Meta class used to associate a model with the form.
		Uses the exclude field to exclude model fields from the form
		'''
		
		model = Advert
		exclude = ("user", "datetime_posted")

class KeywordForm(forms.Form):
	
	# Invalid characters
	chars = [";","/","'",":","]","[","{","}","=","-","_",")","(","*","&","^","%","$",u"£","\"","?","!","`",u"¬",u"¦","\\","|","<",">"]
	
	# Form field
	keyword = forms.CharField(label='Keywords', max_length=220, widget=forms.TextInput(attrs={'placeholder' : 'keyword1, keyword2'}), error_messages={'required' : 'Advert keywords cannot be blank.'})
	
	def clean_keyword(self):
		
		'''
		Form field specific function that validates the advert keywords.
		Checks for invalid characters, and keyword length.
		'''
		
		keyword = self.cleaned_data["keyword"]
		
		for char in self.chars:
			if char in keyword:
				raise forms.ValidationError("Keywords list contains invalid characters.")
				return keyword
		
		list = keyword.split(",")
		keyword_list = []
		for kw in list:
			k = kw.strip().rstrip(".")
			if k == "" or "," in k or len(k) == 1 or k is None:
				raise forms.ValidationError("Invalid keywords. Keywords must be comma separated and at least 2 characters long.")
				return keyword
			
			keyword_list.append(k)
		
		return ",".join(keyword_list)

class DeleteAdvertForm(forms.ModelForm):
	
	'''
	Form associated with the Advert model through the Meta class.
	Used when a user clicks on the delete button when viewing an advert.
	'''
	
	class Meta:
		model = Advert
		fields = []