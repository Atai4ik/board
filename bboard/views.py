from django.http import HttpResponse


def index(request, *args, **kwargs):
    return HttpResponse('Здесь будет выведен список объявлений')
