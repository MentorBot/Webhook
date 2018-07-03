from django.shortcuts import render
from django.contrib import messages


# create views here

def index(request):
    return render(request, '../templates/index.html')


def become_mentor(request):
    return render(request, '../templates/generic.html')

def find_mentor(request):
    return render(request, '../templates/elements.html')

def mentorregister(request):
    return render(request, '../templates/mentorregister.html')

def mentorsearch(request):
    return render(request, '../templates/mentorsearch.html')
