from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm, ProductUpdateForm

from .models import Product

# Create your views here.

# from django.contrib.auth import authenticate, login

# def my_view(request):
# 	username = request.POST['username']
# 	password = request.POST['password']
# 	user = authenticate(request, username=username, password=password)
# 	if user is not None:
# 		login(request, user)
# 		return redirect('/')
# 	else:
# 		return redirect('/login')
# 	return render(request, 'login.html', {})







def product_create_view(request):
	context = {}
	if request.user.is_authenticated:
		context['some_cool_staff'] = "whatever"
	form = ProductForm(request.POST or None)
	print(request.user)
	context['form'] = form
	if form.is_valid():
		form.save()
		form = ProductForm()
		context['added'] = True
		context['form'] = form
	return render(request, 'products/products_create.html', context)


def product_update_view(request, id):
	obj = get_object_or_404(Product, id=id)
	form = ProductUpdateForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'forms':form
	}
	return render(request, 'products/products_create.html', context)


def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, 'products/products_list.html', context)


def product_detail_view(request, id):
	obj = get_object_or_404(Product, id=id)
	context = {
		'obj': obj
	}
	return render(request, 'products/products_detail.html', context)


def product_delete_view(request, id):
	obj = get_object_or_404(Product, id=id)
	if request.method == 'POST':
		obj.delete()
		return redirect('/')
	context = {
		'obj': obj
	}
	return render(request, 'products/products_delete.html', context)


# def dynamic_lookup_view(request, id):
# 	# obj = Product.objects.get(id=id)
# 	# obj = get_object_or_404(Product, id=id)
# 	try:
# 		obj = Product.objects.get(id=id)
# 	except Product.DoesNotExist:
# 		raise Http404
# 	context = {
# 		'object': obj
# 	}
# 	return render(request, 'products/products_detail.html', context)


# def dender_initial_data(request):
# 	initial_data = {
# 		'title': 'This is Awesome title'
# 	}
# 	obj = Product.objects.get(id=1)
# 	form = ProductForm(request.POST or None, instance=obj)
# 	if form.is_valid():
# 		form.save()
# 	context = {
# 		'forms':form
# 	}
# 	return render(request, 'products/products_create.html', context)


# def product_create_view(request):
# 	my_form = RawProductForm()
# 	if request.method == 'POST':
# 		my_form = RawProductForm(request.POST)
# 		if my_form.is_valid():
# 			print(my_form.cleaned_data)
# 			Product.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.error)
# 	context = {
# 		'forms': my_form
# 	}
# 	return render(request, 'products/products_create.html', context)


# def product_create_view(request):
# 	if request.method == 'POST':
# 		# print(request.GET)
# 		# print(request.POST)
# 		my_title = request.POST.get('title')
# 		print(my_title)

# 	context = {}
# 	return render(request, 'products/products_create.html', context)