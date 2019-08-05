from django.http import HttpResponse


def people(request, person):
    return HttpResponse(f'Olá {person}')
