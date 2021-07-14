from django import forms

from . models import Product


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
