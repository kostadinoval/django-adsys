from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from domain.forms import DomainForm
from domain.models import Domain

'''
The add and list views use Django's login_required decorator
to check whether a user is logged in.
Users who are not logged in are redirected to the URL
defined under the login_URL variable in the project settings file.
'''

@login_required
def add(request):
	
	'''
	View which registers a domain through the domain form.
	'''
	
	if request.method == 'POST':
		domainForm = DomainForm(request.POST, request=request)
		
		if domainForm.is_valid():
			
			domain = domainForm.save(commit=False)
			domain.user = request.user
			domain.save()
			return redirect("advert.views.list")
	# Cases where the method wasn't POST generate a blank form
	else:
		domainForm = DomainForm()
	
	return render(request, 'domain/add.html', {'domainForm' : domainForm})

@login_required
def list(request):
	
	'''
	Retrieves all the domains for a given user and
	adds the list to a context dictionary which is
	passed to the template to be displayed.
	'''
	
	domain_list = Domain.objects.filter(user=request.user).order_by("-datetime_posted")
	cd = { "domain_list" : domain_list }
	return render(request, 'domain/list.html', cd)