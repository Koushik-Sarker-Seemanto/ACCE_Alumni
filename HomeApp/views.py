from django.shortcuts import render

from django.shortcuts import redirect, render, HttpResponse

# Create your views here.


def index_view(request):
    return render(request, 'HomeApp/index.html')
