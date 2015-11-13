from django.shortcuts import render
from feedback.forms import FeedbackForm

def post(request):
	
	'''
	View which posts the feedback entered
	in the feedback form. If a user is logged in
	they are referenced in the feedback object.
	'''
	
	if request.method == 'POST':
		
		feedbackForm = FeedbackForm(request.POST)
		if feedbackForm.is_valid():
			if request.user.is_authenticated():
				feedback = feedbackForm.save(commit = False)
				feedback.user = request.user
				feedback.save()
			else:
				feedback = feedbackForm.save()
			
			return render(request, 'feedback/success.html')
	# Not a POST request - provide a blank form
	else:
		feedbackForm = FeedbackForm()
	return render(request, 'feedback/post.html', {'feedbackForm' : feedbackForm})
