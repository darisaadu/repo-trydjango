from django import forms

from django.contrib.auth import get_user_model

from . models import Product


User = get_user_model()

class ProductForm(forms.ModelForm):
	title 		= forms.CharField(label='', widget=forms.TextInput(
						attrs={'placeholder': 'Your title'}))
	description = forms.CharField(required=False, widget=forms.Textarea(
										attrs={
											'placeholder': 'Your Description',
											'class': 'my-new-class-name two',
											'id': 'id-of-textarea',
											'rows': 20,
											'cols': 120
										}
									)
								)
	price 		= forms.DecimalField(initial=99.99)

	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price'
		]

	def clean_title(self):
		title = self.cleaned_data.get('title')
		qs = Product.objects.filter(title__iexact=title)
		if qs.exists():
			raise forms.ValidationError(f'{title} is taken. Try again.')
		# if title.startswith('Tesla'):
		# 	raise forms.ValidationError(f'{title} is taken. Try again.')
		return title


class RawProductForm(forms.Form):
	title 		= forms.CharField(label='', widget=forms.TextInput(
						attrs={'placeholder': 'Your title'}))
	description = forms.CharField(required=False, widget=forms.Textarea(
										attrs={
											'placeholder': 'Your Description',
											'class': 'my-new-class-name two',
											'id': 'id-of-textarea',
											'rows': 20,
											'cols': 120
										}
									))
	price 		= forms.DecimalField(initial=99.99)
