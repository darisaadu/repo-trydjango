from django.http import Http404
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm, ProductUpdateForm

from account.decorator import allower_user, admin_only


from .models import Product


def customer_view(request, *args, **kwargs):
	title = 'My Profile'
	profile = 'This profile at less contain customer picture'
	customer = 'Customers is here!!'
	context = {
		'title': title,
		'customer': customer, 
		'profile': profile
		}
	return render(request, 'products/customer_page.html', context)


@login_required
@admin_only
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

@login_required
@admin_only
def product_update_view(request, id, *args, **kwargs):
	obj = get_object_or_404(Product, id=id)
	form = ProductUpdateForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form':form,
		'obj': obj
	}
	return render(request, 'products/products_update.html', context)

@login_required
def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, 'products/products_list.html', context)

@login_required
def product_detail_view(request, id):
	obj = get_object_or_404(Product, id=id)
	context = {
		'obj': obj
	}
	return render(request, 'products/products_detail.html', context)

@login_required
@admin_only
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