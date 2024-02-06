from django.http import HttpResponse
from django.shortcuts import render
from .models import Gallery


def gallery(request):
    gallery_1 = Gallery.objects.filter(is_visible=True)
    return render(request, 'gallery.html', {'gallery': gallery_1})

