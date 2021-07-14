from django.shortcuts import render

from django.http import HttpResponse

from . models import Reporter, Article

# Create your views here.
def home_view(request, *args, **kwargs):
	if request.user.is_authenticated:
		context = {'name': 'You are logged in'}
	else:
		context = {'name': 'You are logged out'}
	return render(request, 'home.html', context)


# def about_view(request, *args, **kwargs):
# 	queryset = Article.objects.all()
# 	context = {'object': queryset}
# 	return render(request, 'about.html', context)


def contact_view(request, *args, **kwargs):
	return render(request, 'contact.html', {})



def about_view(request, year, month, day):
	a_list = Article.objects.filter(pub_date__year=year)
	context = {
		'year': year, 
		'article_list': a_list, 
		'month':month, 
		'day': day
		}
	return render(request, 'about.html', context)


