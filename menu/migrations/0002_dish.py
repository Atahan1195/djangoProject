# Generated by Django 5.0.1 on 2024-02-01 02:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('is_visible', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, upload_to='menu_dishes')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menucategory')),
            ],
        ),
    ]