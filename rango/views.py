from django.http import HttpResponse

def index(request): 
	link = 'Rango says hey there world!' + '<a href = "/rango/about/">About</a>'
	return HttpResponse(link)
	# each function means a view

def about(request):
	link = 'Rango says here is the about page.' + '<a href = "/rango/">Main</a>'
	return HttpResponse(link)
