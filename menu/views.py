from django.http import HttpResponse
from django.shortcuts import render
from .models import MenuCategory, Dish


def menu(request):
    categories = MenuCategory.objects.filter(is_visible=True)
    return render(request, 'menu.html', {'categories': categories})


def menu_dish(request, slug, id):
    dish = Dish.objects.get(id=id)
    return render(request, 'dish.html', {'dish': dish})
