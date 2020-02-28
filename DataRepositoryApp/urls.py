from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'DataRepositoryApp'


urlpatterns = [

    path('alumni/', views.get_all_alumni, name='get-alumni'),
]
