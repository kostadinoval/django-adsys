from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from advert.models import Advert, AdvertKeyword
from django.contrib.auth.decorators import login_required
from django.utils.html import escape
from advert.forms import AdvertForm, KeywordForm, DeleteAdvertForm
from adverthistory.models import AdvertImpression, AdvertClick
from adspace.models import AdSpace
from domain.models import Domain
from page.models import Page
from adtopage.models import AdToPage

'''
Each view uses Django's @login_required decorator to check if the user is authenticated.
Users who are not authenticated are redirected to the login_URL defined in the settings file,
otherwise the specific view code is executed
'''

@login_required
def list(request):
	
	'''
	Retrieves all the adverts for a given user and
	adds the list to a context dictionary which is
	passed to the template to be displayed.
	'''
	
	advert_list = Advert.objects.filter(user = request.user).order_by("-datetime_posted")
	cd = {"adverts" : advert_list}
	return render(request, 'advert/list.html', cd)

@login_required
def create(request):
	
	'''
	Combines an advertForm and a keywordForm to
	collect input from the user about each new advert.
	Processes the comma separated list of keywords
	to create advertkeyword objects.
	Creates objects from the advertclick and
	advertimpression models
	'''
	
	if request.method == 'POST':
		
		advertForm = AdvertForm(request.POST, request=request)
		keywordForm = KeywordForm(request.POST)
		
		if advertForm.is_valid() and keywordForm.is_valid():
			
			advert = advertForm.save(commit = False)
			
			advert.user = request.user
			advert.save()
			
			keywords = keywordForm.cleaned_data["keyword"]
			
			temp = keywords.split(",")
			keywordList = []
			for t in temp:
				keywordList.append(t)
			
			for keyword in keywordList:
				temp = AdvertKeyword(advert = advert, keyword = keyword)
				temp.save()
			
			ad_i = AdvertImpression(advert = advert)
			ad_i.save()
			
			ad_c = AdvertClick(advert = advert)
			ad_c.save()
			
			return redirect("advert.views.list")
	# Not a POST request - render empty forms
	else:
		
		advertForm = AdvertForm()
		keywordForm = KeywordForm()
	
	return render(request, 'advert/add.html', {'advertForm' : advertForm, 'keywordForm' : keywordForm})

@login_required
def view(request, advert_id):
	
	'''
	Retrieves all the details of a specific advert.
	advert_id is passed as a URL path segment.
	Passes an instance of the DeleteAdvertForm to allow
	the user to delete the advert.
	'''
	
	advert = get_object_or_404(Advert, pk = advert_id, user = request.user)
	
	keywords_list = AdvertKeyword.objects.filter(advert = advert).order_by("pk")
	
	deleteAdvertForm = DeleteAdvertForm(instance=advert)
	
	cd = {"advert" : advert, "keywords_list" : keywords_list, "deleteAdvertForm" : deleteAdvertForm}
	
	return render(request, 'advert/view.html', cd)

@login_required
def delete(request, advert_id):
	
	'''
	Deletes a specific advert based on the advert_id.
	This is passed as a URL path segment
	'''
	
	advert = get_object_or_404(Advert, pk = advert_id, user = request.user)
	
	if request.method == 'POST':
		deleteAdvertForm = DeleteAdvertForm(request.POST, instance = advert)
		
		if deleteAdvertForm.is_valid():
			advert.delete()
			
			return redirect("advert.views.list")
	
	return redirect("advert.views.view", advert_id = advert_id)

@login_required
def edit(request, advert_id = None):
	
	'''
	Provides the functionality of editing and advert.
	Processes the submitted forms and updates the required fields.
	'''
	
	if advert_id:
		
		advert = get_object_or_404(Advert, pk = advert_id, user = request.user)
		
		
		list = []
		keywords = AdvertKeyword.objects.filter(advert = advert).order_by("pk")
		
		for keyword in keywords:
			list.append(keyword.keyword)
		
		string_list = ",".join(list)
		
		
		if request.method == 'POST':
			advertForm = AdvertForm(request.POST, instance=advert, request=request, edit=True, advert_id=advert.pk)
			keywordForm = KeywordForm(request.POST)
			
			if advertForm.is_valid() and keywordForm.is_valid():
				advert = advertForm.save()
				
				AdvertKeyword.objects.filter(advert = advert).delete()
				
				keywords = keywordForm.cleaned_data["keyword"]
				temp = keywords.split(",")
				keywordList = []
				for t in temp:
					keywordList.append(t.strip())
				
				for keyword in keywordList:
					temp = AdvertKeyword(advert = advert, keyword = keyword)
					temp.save()
				
				return redirect("advert.views.list")
		
		else:
			advertForm = AdvertForm(instance = advert, request=request)
			keywordForm = KeywordForm(initial={"keyword" : string_list})
		
		cd = {"advertForm" : advertForm, "keywordForm" : keywordForm, "advert" : advert, "keywords" : string_list}
		
		return render(request, "advert/edit.html", cd)

def getAdvert(request):
	
	'''
	View called via AJAX.
	Used to retrieve the specific advert
	to be served on the requesting page.
	
	AJAX passes three get parameters
	url = page url
	data_aid = adspace id
	data_uid = user id
	'''
	
	url = None
	data_aid = None
	data_uid = None
	
	if request.method == 'GET':
		url = request.GET["url"]
		data_aid = request.GET["data_aid"]
		data_uid = request.GET["data_uid"]
		
		user = None
		adspace = None
		found_domain = False
		
		try:
			user = User.objects.get(pk = data_uid)
		except User.DoesNotExist:
			user = None
		
		if user:
			
			domains = Domain.objects.filter(user = user)
			for domain in domains:
				if domain.domain.strip("http://").strip("https://").strip("www.") in url:
					found_domain = True
					try:
						adspace = AdSpace.objects.get(pk = data_aid, user = user)
					except AdSpace.DoesNotExist:
						adspace = None
		
		if adspace and found_domain:
			page = None
			try:
				page = Page.objects.get(pageURL = url)
			except Page.DoesNotExist:
				page = None
			if page is not None:
				
				adtopage = AdToPage.objects.get(page = page, active = True)
				advert = Advert.objects.get(pk = adtopage.advert.pk)
				cd = {"title" : advert.title, "description" : advert.description, "destination_url" : advert.destination_url}
				return JsonResponse(cd)
	# An error occurred in the process
	return JsonResponse({"error" : "Invalid User, AdSpace Code or URL!"})

def getEscaped(request):
	
	'''
	View called via AJAX.
	Used in the Create and Edit advert, Create AdSpace.
	Escapes user input to be displayed in the preview box.
	Returns JSON Object
	'''
	
	return JsonResponse({"data" : escape(request.GET["data"])})
