from django.shortcuts import render

from django.shortcuts import redirect, render, HttpResponse
from .models import Carousel, Notice, Gallery
# Create your views here.


def index_view(request):
    carousels = Carousel.objects.all().order_by('-created_at')[:3]
    events = Notice.objects.all().order_by('-created_at')[:5]
    carousels = list(carousels)
    # print(carousels)

    context = {
        "carousels": carousels,
        "events": events,
    }
    return render(request, 'HomeApp/index.html', context)


def upcoming_events(request, pk):
    if pk == 0:
        current_event = Notice.objects.all().order_by('-created_at')[:1].get()
        events = Notice.objects.all().exclude(pk=current_event.pk).order_by('-created_at')[:5]
    else:
        current_event = Notice.objects.get(pk=pk)
        events = Notice.objects.all().exclude(pk=pk).order_by('-created_at')[:5]
    context = {
        "events": events,
        "current_event": current_event
    }
    return render(request, 'HomeApp/UpcomingEventPage.html', context)


def gallery_view(request):
    notices = Notice.objects.all().order_by('-created_at')
    list_of_event = []
    for i in notices:
        gallery_by_event = Gallery.objects.filter(event=i)
        list_of_event.append((i, gallery_by_event))

    context = {
        "notices": notices,
        "list_of_event": list_of_event,
    }
    return render(request, 'HomeApp/GalleryPage.html', context)


def about_us_view(request):
    context = {

    }
    return render(request, 'HomeApp/AboutPage.html', context)


def contact_view(request):
    return render(request, 'HomeApp/ContactPage.html')

