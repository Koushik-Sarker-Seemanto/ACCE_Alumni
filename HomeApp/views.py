from django.shortcuts import render

from django.shortcuts import redirect, render, HttpResponse
from  .models import Carousel, Notice
# Create your views here.


def index_view(request):
    carousels = Carousel.objects.all().order_by('-created_at')[:3]
    events = Notice.objects.all().order_by('-created_at')[:5]
    carousels = list(carousels)
    print(carousels)
    context = {
        "carousels": carousels,
        "events": events,
    }
    return render(request, 'HomeApp/index.html', context)


def upcoming_events(request, pk):
    events = Notice.objects.all().order_by('-created_at')[:5]
    current_event = Notice.objects.get(pk=pk)
    context = {
        "events": events,
        "current_event": current_event
    }
    return render(request, 'HomeApp/UpcomingEventPage.html', context)

