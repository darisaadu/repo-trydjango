from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import Product

# Create your views here.


def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		'forms':form
	}
	return render(request, 'products/products_create.html', context)


def product_update_view(request, id):
	obj = get_object_or_404(Product, id=id)
	form = ProductForm(request.POST or None, instance=obj)
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
		'objects': obj
	}
	return render(request, 'products/products_detail.html', context)


def product_delete_view(request, id):
	obj = get_object_or_404(Product, id=id)
	if request.method == 'POST':
		obj.delete()
		return redirect('../../')
	context = {
		'objects': obj
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