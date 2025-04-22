
from django.shortcuts import render
from django.http import HttpResponse

def about_view(request):
    return render(request, 'about.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def experience_view(request):
    return render(request, 'experience.html')


