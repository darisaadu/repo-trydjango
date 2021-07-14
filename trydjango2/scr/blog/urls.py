from django.urls import path
from .views import (
	ArticleCreateView,
	ArticleUpdateView,
	ArticleDetailView,
    ArticleListView,
    ArticleDeletelView
)


app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-upudate'),
    path('<int:id>/delete/', ArticleDeletelView.as_view(), name='article-delete'),
] 