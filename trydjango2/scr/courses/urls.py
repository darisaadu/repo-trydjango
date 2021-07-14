from django.urls import path
from .views import (
    CourseView,
    CourseCreateView,
    CourseUpdateView,
    CourseListView,
    CourseDeleteView
    # my_fbv
)


app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    # path('', my_fbv, name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    path('create/', CourseCreateView.as_view(), name='create-list'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-upudate'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='course-delete'),
] 