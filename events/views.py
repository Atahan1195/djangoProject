from django.http import HttpResponse
from django.shortcuts import render


def events(request):
    return HttpResponse("Future events page")
