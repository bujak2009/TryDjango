from django.contrib import admin
from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    my_fbv,
    CourseCreateView,
    CourseUpdateView
)


app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('', my_fbv, name='courses-list'),
    path('<int:id>/', CourseDetailView.as_view(), name='course-detail'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-update'),

]