from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('course/<int:course_id>/enroll/',views.enroll,name='enroll'),
    path('my-courses/', views.my_courses, name='my_courses'),
]