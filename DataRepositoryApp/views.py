from django.shortcuts import render

from django.shortcuts import redirect, render, HttpResponse
from DataRepositoryApp.models import Alumni

# Create your views here.


def get_all_alumni(request):
    all_people = Alumni.objects.all()

    context = {
        'all_people': all_people
    }
    return render(request, 'DataRepositoryApp/AlumniPage.html', context)
