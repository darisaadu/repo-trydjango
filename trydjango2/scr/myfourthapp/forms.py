from django import forms

from . models import MyProduct


class MyProductForm(forms.ModelForm):
	title = forms.CharField(label='', widget=forms.TextInput(
							attrs={'placeholder':'Your title'}))
	content = forms.CharField(widget=forms.Textarea(attrs={
		'placeholder': 'Your Text',
		'class': 'my-new-class 2',
		'id': 'my-second-id',
		'rows': 16,
		'cols': 80
		}))
	price = forms.DecimalField(initial=99.99)
	class Meta:
		model = MyProduct
		fields = [
			'title',
			'content',
			'price'
		]


	def clean_title(self):
		title = self.cleaned_data.get('title')
		if 'abc' in title:
			raise forms.ValidationError('This is invalid title')
		return title


	def clean_content(self):
		content = self.cleaned_data.get('content')
		if len(content) < 5:
			raise forms.ValidationError('Invalid content')
		return content
