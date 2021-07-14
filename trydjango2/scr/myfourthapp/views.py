from django.shortcuts import render, get_object_or_404, redirect
from . models import MyProduct 
# Create your views here.
from django.http import HttpResponse
from . forms import MyProductForm
from django.views import View


# from django.views.generic.base import TemplateView



# class MyViews(TemplateView):
# 	template_name = 'another.html'

# 	def get(self, request, *args, **kwargs):
# 		context = super(MyViews, self).get_context_data(**kwargs)
# 		context['latest_articles'] = MyProduct.objects.all()[::2][:3][:1]
# 		# return context
# 		return render(request, self.template_name, context)



class MyProductCreateView(View):
	template_name = 'myproduct_create.html'


	def get(self, request, *args, **kwargs):
		form = MyProductForm()
		context = {'form': form}
		return render(request, self.template_name, context)


	def post(self, request, *args, **kwargs):
		form = MyProductForm(request.POST or None)
		if form.is_valid():
			form.save()
			form = MyProductForm()
			return redirect('/myfourthapp/')
		context = {'form': form}
		return render(request, self.template_name, context)


class MyProductDetailView(View):
	template_name = 'myproduct_detail.html'

	def get_object(self):
		context = {}
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(MyProduct, id=id)
		return obj 

	def get(self, request, id=None, *args, **kwargs):
		context = {}
		obj = self.get_object()
		if id is not None:
			context['object'] = obj 
		return render(request, self.template_name, context)


class MyProductListView(View):
	template_name = 'myproduct_list.html'
	queryset = MyProduct.objects.all()


	def get_object(self):
		return self.queryset


	def get(self, request, *args, **kwargs):
		context = {'objects_list': self.get_object}
		return render(request, self.template_name, context)

