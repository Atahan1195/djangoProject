from django.db import models


class MenuCategory(models.Model):
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    name = models.CharField(max_length=50, unique=True)
    position = models.PositiveSmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __iter__(self):
        for dish in self.dishes.filter(is_visible=True):
            yield dish

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return self.name


class Dish(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=60, unique=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='dishes')
    position = models.PositiveSmallIntegerField(unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    ingredients = models.TextField()
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='menu_dishes', blank=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return self.name



