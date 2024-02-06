from django.contrib import admin
from menu.models import MenuCategory, Dish


@admin.register(MenuCategory)
class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



