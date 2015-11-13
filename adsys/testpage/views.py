from django.shortcuts import render

def pageA(request):
	return render(request, 'testpage/page_a.html')

def pageB(request):
	return render(request, 'testpage/page_b.html')

def pageC(request):
	return render(request, 'testpage/page_c.html')

def page(request):
	return render(request, 'testpage/page.html')
