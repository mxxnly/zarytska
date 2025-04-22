from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contact'),
    path('experience/', views.experience_view, name='exp'),
]
