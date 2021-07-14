
from django.urls import path
from . views import (
		MyProductListView,
		MyProductDetailView,
		MyProductCreateView
		)   

app_name = 'myfourthapp'
urlpatterns = [
    # path('hello/<int:pk>/', MyView.as_view()),
	path('', MyProductListView.as_view(), name='myproduct-list'),
	path('create/', MyProductCreateView.as_view(), name='myproduct-create'), 
	path('<int:id>/', MyProductDetailView.as_view(), name='myproduct-detail') 

]