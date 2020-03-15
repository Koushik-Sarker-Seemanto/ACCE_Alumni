from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'HomeApp'


urlpatterns = [

    path('', views.index_view, name='home'),
    path('events/<int:pk>/', views.upcoming_events, name='upcoming-event'),
    path('gallery/', views.gallery_view, name='gallery-view'),
]
