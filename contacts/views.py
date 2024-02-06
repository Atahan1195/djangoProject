from django.http import HttpResponse
from django.shortcuts import render


def contacts(request):
    return render(request, 'layouts/contact.html')
