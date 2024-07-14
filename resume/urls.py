
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('certificates/', views.certificates, name='certificates'),
    path('projects/', views.projects, name='projects'),
    path('feedback/', views.feedback, name='feedback'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),  # Add this line
    path('success/', views.success_page, name='success_page'),  # Define success page URL here
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
]