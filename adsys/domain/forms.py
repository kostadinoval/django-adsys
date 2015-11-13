from django import forms
from domain.models import Domain

class DomainForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		
		self.request = kwargs.pop('request', None)
		super(DomainForm, self).__init__(*args, **kwargs)
	
	domain = forms.URLField(label = 'Domain', error_messages={'required' : 'The domain is required.'})
	
	def clean_domain(self):
		
		'''
		Form field specific function that validates domains.
		It checks to make sure that the user hasn't already registered
		the same domain.
		'''
		
		domain = self.cleaned_data["domain"]
		domain_count = Domain.objects.filter(user=self.request.user, domain__iexact=domain).count()
		if domain_count != 0:
			raise forms.ValidationError("You have already registered this domain.")
		
		return domain
	
	class Meta:
		
		'''
		Associate this form with the domain model.
		The exclude tuple provides a list of fields to exclude from the form.
		'''
		
		model = Domain
		exclude = ("user", "crawled", "datetime_posted",)
