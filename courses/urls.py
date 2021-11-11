
from django.urls import path
from .views import (CourseView,
                    CourseListView,
                    CourseCreateView,
                    CourseDeleteView,
                    CourseUpdateView)
app_name = "courses"
urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),
    path("create/", CourseCreateView.as_view(), name="article-create"),
    path("<int:id>", CourseView.as_view() , name="course-detail"),
    path("<int:id>/update", CourseUpdateView.as_view(), name="article-update"),
    path("<int:id>/delete", CourseDeleteView.as_view(), name="article-delete"),
]
