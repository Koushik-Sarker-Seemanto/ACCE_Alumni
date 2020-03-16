from django.shortcuts import render

from django.shortcuts import redirect, render, HttpResponse
from DataRepositoryApp.models import Alumni

# Create your views here.


def get_all_alumni(request):
    list_of_people = []
    session_list = []
    for i in range(2020, 1972, -1):
        session = str(i)+'-'+str((i+1) % 1000)
        session_list.append(session)
        session_wise = Alumni.objects.filter(session__icontains=str(i))
        list_of_people.append((session, session_wise))
    # print(list_of_people)
    # print(session_list)
    context = {
        'list_of_people': list_of_people,
        'session_list': session_list,
    }
    return render(request, 'DataRepositoryApp/AlumniPage.html', context)


def get_by_session(request, session):
    all_people = Alumni.objects.filter(session=session)

    context = {
        'current_session': session,
        'all_people': all_people
    }
    return render(request, 'DataRepositoryApp/BatchPage.html', context)


def get_profile_by_id(request, pk):
    people = Alumni.objects.get(pk=pk)

    context = {
        'people': people
    }
    return render(request, 'DataRepositoryApp/Profile.html', context)


def search_result(request):
    search_key = request.GET.get('search_field')
    search_by_name = Alumni.objects.filter(name__icontains=search_key)
    search_by_session = Alumni.objects.filter(session__icontains=search_key)
    search_by_position = Alumni.objects.filter(current_position__icontains=search_key)
    context = {
        'search_by_name': search_by_name,
        'search_by_session': search_by_session,
        'search_by_position': search_by_position,
        'search_key': search_key
    }

    return render(request, 'DataRepositoryApp/SearchResultPage.html', context)
