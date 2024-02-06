from django.urls import path
from .views import menu, menu_dish


urlpatterns = [
    path('', menu, name='menu'),
    path('<slug:slug>/<int:id>/', menu_dish, name='menu_dish')
]