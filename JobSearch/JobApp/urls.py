from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('job_category/', views.job_category, name="job_category"),
    path('job_detail/', views.job_detail, name="job_detail"),
    path('about_us/', views.about_us, name="about_us"),
    path('contact/', views.contact, name="contact"),
    path('post_job/', views.post_job, name="post_job"),
]
