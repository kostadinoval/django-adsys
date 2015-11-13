from django.shortcuts import render

'''

Two views rendering static HTML templates
Both return a render object with the request and the corresponding template

'''

def about(request):
	
	return render(request, 'about/about.html')

def faq(request):
	
	return render(request, 'about/faq.html')