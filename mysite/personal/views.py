from django.shortcuts import render

def index(request):
	return render(request, 'personal/home.html')


def contact(request):
	return render(request, 'personal/contactme.html', {'contactinfo': ["If you would like to contact me, please email me.", "rannie.xue@gmail.com"]})