from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from adspace.forms import AdSpaceForm, DeleteAdSpaceForm
from adspace.models import AdSpace

'''
Each view uses Django's @login_required decorator to check if the user is authenticated.
Users who are not authenticated are redirected to the login_URL defined in the settings file,
otherwise the specific view code is executed
'''

@login_required
def list(request):
	
	'''
	Retrieves all the adspaces for a given user and
	adds the list to a context dictionary which is
	passed to the template to be displayed.
	'''
	
	adspace_list = AdSpace.objects.filter(user = request.user).order_by("-datetime_posted")
	cd = {"adspaceList" : adspace_list}
	return render(request, 'adspace/list.html', cd)

@login_required
def create(request):
	
	'''
	Creates an adspace based on the user input from the
	adspaceForm. Generates the required adspace code.
	'''

	if request.method == 'POST':
		
		adspaceForm = AdSpaceForm(request.POST, request=request)
		
		if adspaceForm.is_valid():
			
			title = adspaceForm.cleaned_data["title"]
			
			colour = adspaceForm.cleaned_data["adspace_border_colour"]
			size = adspaceForm.cleaned_data["adspace_size"]
			
			if size == "1":
				width = 320
				height = 400
			elif size == "2":
				width = 430
				height = 300
			elif size == "3":
				width  = 250
				height = 515
			else:
				width = 0
				height = 0
			
			'''
			The new adspace is saved initially with an empty adspace_code
			This is because the adspace code requires the adspace id
			which is only available after creating and saving an adspace
			'''
			new_adspace = AdSpace(user=request.user, title=title, width=width, height=height, border_colour=colour, adspace_code="")
			
			new_adspace.save()
			
			adspace_code = '<script>$(document).ready(function(){var url = window.location.href; var element = document.getElementById("__adspace"); var data-aid = element.getAttribute("data-aid"); var data-uid = element.getAttribute("data-uid"); $.get("adverts.views.getAdvert", {"url" : url, "data-aid" : data-aid, "data-uid" : data-uid}, function(data){alert(1);})});</script><div id = "__adspace" data-aid="' + str(new_adspace.pk) + '" data-uid="' + str(request.user.pk) + '" style="width:' + str(width) + 'px; height:' + str(height) + 'px; border-style:solid; border-color:' + str(colour) + '; text-align:justify;"><a class="__advert_url" href=""><p id="__advert_title" style="font-weight:bold; font-size:24px; margin:20px;"></p></a><a class="__advert_url" style="font-decoration:none;" href=""><p id="__advert_description" style="font-size:19px; margin:20px;"></p></a><a class="__advert_url" style="font-decoration:none;" href=""><p id="__advert_destination_url" style="font-size:19px; margin:20px;"></p></a></div>'
			
			new_adspace.adspace_code = adspace_code
			
			new_adspace.save()
			
			return redirect("adspace.views.list")
	
	# request method was GET therefore generate a new adspace form
	else:
		adspaceForm = AdSpaceForm(initial={'adspace_size' : '1'})
	
	return render(request, 'adspace/add.html', {'adspaceForm' : adspaceForm})

@login_required
def view(request, adspace_id):
	
	'''
	Retrieves all the details of a specific adspace.
	adspace_id is passed as a URL path segment.
	Passes an instance of the deleteAdSpaceForm to allow
	the user to delete the adspace.
	'''
	
	adspace = get_object_or_404(AdSpace, pk = adspace_id, user = request.user)
	
	deleteAdSpaceForm = DeleteAdSpaceForm(instance = adspace)
	cd = {"adspace" : adspace, "deleteAdSpaceForm" : deleteAdSpaceForm}
	
	return render(request, 'adspace/view.html', cd)

@login_required
def delete(request, adspace_id):
	
	'''
	Deletes a specific adspace based on the adspace_id.
	This is passed as a URL path segment
	'''
	
	adspace = get_object_or_404(AdSpace, pk = adspace_id, user = request.user)
	
	if request.method == 'POST':
		deleteAdSpaceForm = DeleteAdSpaceForm(request.POST, instance = adspace)
		
		if deleteAdSpaceForm.is_valid():
			adspace.delete()
			
			return redirect("adspace.views.list")
	
	return redirect("adspace.views.view", adspace_id = adspace_id)
